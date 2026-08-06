#!/usr/bin/env python3
"""縦型ショート（1080x1920）を本編MP4からレンダリングする。

第1作『放課後トークルーム』で実測済みの手順を一般化したもの。
前提: pip install imageio-ffmpeg pillow
      日本語フォント（例: japanize-matplotlib の sdist から ipaexg.ttf を抽出）

使い方:
  python3 render_short.py --master master.mp4 --font jp.ttf --out short.mp4 \
      --loop-seconds 10.041667 --loops 3 --captions captions.json

captions.json の形式（band は "top" か "bottom"）:
  [
    {"start": 0.0, "end": 2.5, "band": "top",
     "lines": ["雑談配信のBGM、", "決まってる？"], "size": 92},
    ...
  ]

設計原則:
- 尺 = 映像ループ周期 × 整数。ショート自体がシームレスにループする
- 素材は SHA-256 照合済みの Release 版本編だけ。低画質版を使わない
- レンダ後は必ず各テロップ区間のフレームを抜いて目視検品する
"""
import argparse, json, subprocess, sys

def build_caption_png(font_path, spec, path, W=1080, H=1920):
    from PIL import Image, ImageDraw, ImageFont
    PINK = (224, 80, 122, 255)
    WHITE = (255, 255, 255, 255)
    SHADOW = (60, 30, 40, 120)
    img = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    y = 330 if spec.get('band', 'top') == 'top' else 1340
    for text in spec['lines']:
        size = spec.get('size', 64)
        font = ImageFont.truetype(font_path, size)
        sw = int(size * 0.12)
        w = d.textbbox((0, 0), text, font=font, stroke_width=sw)[2]
        x = (W - w) // 2
        d.text((x + 5, y + 6), text, font=font, fill=SHADOW, stroke_width=sw, stroke_fill=SHADOW)
        d.text((x, y), text, font=font, fill=WHITE, stroke_width=sw, stroke_fill=PINK)
        y += int(size * 1.32)
    img.save(path)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--master', required=True)
    ap.add_argument('--font', required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--loop-seconds', type=float, required=True, help='映像ループ1周の秒数')
    ap.add_argument('--loops', type=int, default=3)
    ap.add_argument('--captions', required=True)
    ap.add_argument('--fps', type=int, default=24)
    args = ap.parse_args()

    import imageio_ffmpeg
    ff = imageio_ffmpeg.get_ffmpeg_exe()
    dur = args.loop_seconds * args.loops

    caps = json.load(open(args.captions, encoding='utf-8'))
    inputs = ['-ss', '0', '-t', f'{dur:.3f}', '-i', args.master]
    for i, c in enumerate(caps):
        png = f'cap{i}.png'
        build_caption_png(args.font, c, png)
        inputs += ['-i', png]

    fc = ("[0:v]split=2[bgs][fgs];"
          "[bgs]scale=1080:1920:force_original_aspect_ratio=increase,"
          "crop=1080:1920,gblur=sigma=28,eq=brightness=-0.06[bg];"
          "[fgs]scale=1080:-2[fg];"
          "[bg][fg]overlay=(W-w)/2:(H-h)/2[v0];")
    prev = 'v0'
    for i, c in enumerate(caps):
        nxt = f'v{i+1}'
        fc += f"[{prev}][{i+1}:v]overlay=0:0:enable='between(t,{c['start']},{c['end']})'[{nxt}];"
        prev = nxt
    fade_start = dur - 0.325
    fc += f"[0:a]afade=t=out:st={fade_start:.3f}:d=0.325[aout]"

    cmd = [ff, '-v', 'error', '-y'] + inputs + [
        '-filter_complex', fc, '-map', f'[{prev}]', '-map', '[aout]',
        '-c:v', 'libx264', '-crf', '19', '-preset', 'medium',
        '-r', str(args.fps), '-pix_fmt', 'yuv420p',
        '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart', args.out]
    subprocess.run(cmd, check=True)
    print(f'rendered: {args.out} ({dur:.3f}s)')
    print('次: 各テロップ区間のフレームを抽出して目視検品すること')

if __name__ == '__main__':
    sys.exit(main())
