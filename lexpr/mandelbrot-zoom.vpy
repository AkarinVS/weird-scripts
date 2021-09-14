# This is a translated Mandelbrot zoomer on http://avisynth.nl/index.php/Expr#Examples
# Original AVS+ code:
#   a="X dup * Y dup * - A + T^ X Y 2 * * B + 2 min Y^ T 2 min X^ "
#   b=a+a
#   c=b+b
#   blankclip(width=960,height=640,length=1600,pixel_type="YUV420P8")
#   Expr("sxr 3 * 2 - -1.2947627 - 1.01 frameno ^ / -1.2947627 + A@ X^ syr 2 * 1 - 0.4399695 "
#   \ + "- 1.01 frameno ^ / 0.4399695 + B@ Y^ "+c+c+c+c+c+b+a+"X dup * Y dup * + 4 < 0 255 ?",
#   \ "128", "128")
import vapoursynth as vs
core = vs.core

# AVS Expr+ translation tips:
# X: local variable read, translate to `X@`.
# X@: local variable write without popping stack, translate to `dup X!`.
# X^: local variable write, translate to `X!`.
# sxr: translate to `X width /`
# syr: translate to `Y height /`
# frameno: translate to `N`

a="X@ dup * Y@ dup * - A@ + T! X@ Y@ 2 * * B@ + 2 min Y! T@ 2 min X! "
b=a+a
c=b+b

core.std.BlankClip(width=1920, height=1080, length=500, format=vs.YUV420P8).akarin.Expr([
    "X width / sxr! "      # emulate sxr
        "Y height / syr! " # emulate syr
        "N frameno! "      # emulate frameno
        "sxr@ 3 * 2 - -1.2947627 - 1.01 frameno@ pow / -1.2947627 + dup A! X! syr@ 2 * 1 - 0.4399695 "
        "- 1.01 frameno@ pow / 0.4399695 + dup B! Y! "+c+c+c+c+c+b+a+"X@ dup * Y@ dup * + 4 < 0 255 ?",
    "128",
    "128",
]).set_output()
