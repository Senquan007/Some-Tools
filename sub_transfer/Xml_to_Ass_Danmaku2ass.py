'''
该转换只针对单个文件
'''

# 导入danmaku2ass模块
import danmaku2ass

# 定义输入和输出文件路径
input_file = 'input.xml'
output_file = 'output.ass'

# 调用Danmaku2ASS函数进行转换
# 设置参数，这里使用了一些默认值，你可以根据需要修改它们
danmaku2ass.Danmaku2ASS(
    input_files=input_file,                  # 输入文件路径
    input_format='autodetect',              # 自动检测输入格式
    output_file=output_file,                # 输出文件路径
    stage_width=1920,                       # 舞台宽度
    stage_height=1080,                      # 舞台高度
    font_size=35.0,                         # 字体大小
    text_opacity=0.8,                       # 文本不透明度
    duration_marquee=10.0,                  # 滚动弹幕显示的持续时间
    duration_still=5.0,                    # 静止弹幕显示的持续时间
    reserve_blank=0,                       # 保留底部空白高度
    font_face='黑体'                      # 字体名称
)

print(f"Successfully converted {input_file} to {output_file}")