from PIL import Image

def crop_image(input_image_path, output_image_path1, output_image_path2, crop_size):
    # 打开原始图像
    original_image = Image.open(input_image_path)
    
    # 获取原始图像的尺寸
    original_width, original_height = original_image.size  # 这里是600*400

    # 计算裁剪区域的起始点
    # 假设我们从图像的左上角和右下角分别裁剪
    left_top_x = 0
    left_top_y = 0
    right_bottom_x = crop_size*3/2
    right_bottom_y = crop_size
    
    # 裁剪第一个图像区域
    crop1 = original_image.crop((left_top_x, left_top_y, right_bottom_x, right_bottom_y))
    # crop1 = original_image.crop((0, 0, 540, 360))

    # 计算第二个图像区域的起始点，位于图像的右下角
    left_top_x = original_width - crop_size*3/2
    left_top_y = original_height - crop_size
    right_bottom_x = original_width
    right_bottom_y = original_height
    
    # 裁剪第二个图像区域
    crop2 = original_image.crop((left_top_x, left_top_y, right_bottom_x, right_bottom_y))
    # crop2 = original_image.crop((60, 40, 600, 400))
    
    # 保存裁剪后的图像
    crop1.save(output_image_path1)
    crop2.save(output_image_path2)

""" # 使用示例LOL1
input_path = '/home/xr/KXR/SuperGluePretrainedNetwork/LOL_data/LOL_v1/RetinexMamba_LOL_v1/best_psnr_23/1.png'  # 替换为你的图像文件路径
output_path1 = '/home/xr/KXR/SuperGluePretrainedNetwork/LOL_breakdata/LOL_v1/image1.png'    # 第一个输出图像的路径
output_path2 = '/home/xr/KXR/SuperGluePretrainedNetwork/LOL_breakdata/LOL_v1/image2.png'    # 第二个输出图像的路径
crop_dimensions = 360  # 裁剪区域的高度，不能超过400

crop_image(input_path, output_path1, output_path2, crop_dimensions)

# 使用示例LOL2
input_path = '/home/xr/KXR/SuperGluePretrainedNetwork/LOL_data/LOL_v2_real/RetinexMamba_LOL_v2_real/best_psnr_21/00690.png'  # 替换为你的图像文件路径
output_path1 = '/home/xr/KXR/SuperGluePretrainedNetwork/LOL_breakdata/LOL_v2_real/image1.png'    # 第一个输出图像的路径
output_path2 = '/home/xr/KXR/SuperGluePretrainedNetwork/LOL_breakdata/LOL_v2_real/image2.png'    # 第二个输出图像的路径
crop_dimensions = 360  # 裁剪区域的高度，不能超过400

crop_image(input_path, output_path1, output_path2, crop_dimensions)

# 使用示例LOL2_synthetic
input_path = '/home/xr/KXR/SuperGluePretrainedNetwork/LOL_data/LOL_v2_synthetic/RetinexMamba_LOL_v2_synthetic/best_psnr_25/r068812d7t.png'  # 替换为你的图像文件路径
output_path1 = '/home/xr/KXR/SuperGluePretrainedNetwork/LOL_breakdata/LOL_v2_synthetic/image1.png'    # 第一个输出图像的路径
output_path2 = '/home/xr/KXR/SuperGluePretrainedNetwork/LOL_breakdata/LOL_v2_synthetic/image2.png'    # 第二个输出图像的路径
crop_dimensions = 252  # 裁剪区域的高度，不能超过400 """

# 原始数据LOL1
input_path = '/home/xr/KXR/SuperGluePretrainedNetwork/LOL_origin/LOLv1/Test/input/1.png'  # 替换为你的图像文件路径
output_path1 = '/home/xr/KXR/SuperGluePretrainedNetwork/LOL_breakdata/LOL_v1/origin1.png'    # 第一个输出图像的路径
output_path2 = '/home/xr/KXR/SuperGluePretrainedNetwork/LOL_breakdata/LOL_v1/origin2.png'    # 第二个输出图像的路径
crop_dimensions = 360  # 裁剪区域的高度，不能超过400

crop_image(input_path, output_path1, output_path2, crop_dimensions)

# 原始数据LOL2
input_path = '/home/xr/KXR/SuperGluePretrainedNetwork/LOL_origin/LOLv2/Real_captured/Test/Low/00690.png'  # 替换为你的图像文件路径
output_path1 = '/home/xr/KXR/SuperGluePretrainedNetwork/LOL_breakdata/LOL_v2_real/origin1.png'    # 第一个输出图像的路径
output_path2 = '/home/xr/KXR/SuperGluePretrainedNetwork/LOL_breakdata/LOL_v2_real/origin2.png'    # 第二个输出图像的路径
crop_dimensions = 360  # 裁剪区域的高度，不能超过400

crop_image(input_path, output_path1, output_path2, crop_dimensions)

# 原始数据LOL2_synthetic
input_path = '/home/xr/KXR/SuperGluePretrainedNetwork/LOL_origin/LOLv2/Synthetic/Test/Low/r068812d7t.png'  # 替换为你的图像文件路径
output_path1 = '/home/xr/KXR/SuperGluePretrainedNetwork/LOL_breakdata/LOL_v2_synthetic/origin1.png'    # 第一个输出图像的路径
output_path2 = '/home/xr/KXR/SuperGluePretrainedNetwork/LOL_breakdata/LOL_v2_synthetic/origin2.png'    # 第二个输出图像的路径
crop_dimensions = 252  # 裁剪区域的高度，不能超过400

crop_image(input_path, output_path1, output_path2, crop_dimensions)




# 原始数据LOL1
input_path = '/home/xr/KXR/SuperGluePretrainedNetwork/LOL_origin/LOLv1/Test/target/1.png'  # 替换为你的图像文件路径
output_path1 = '/home/xr/KXR/SuperGluePretrainedNetwork/LOL_breakdata/LOL_v1/normal1.png'    # 第一个输出图像的路径
output_path2 = '/home/xr/KXR/SuperGluePretrainedNetwork/LOL_breakdata/LOL_v1/normal2.png'    # 第二个输出图像的路径
crop_dimensions = 360  # 裁剪区域的高度，不能超过400

crop_image(input_path, output_path1, output_path2, crop_dimensions)

# 原始数据LOL2
input_path = '/home/xr/KXR/SuperGluePretrainedNetwork/LOL_origin/LOLv2/Real_captured/Test/Normal/00690.png'  # 替换为你的图像文件路径
output_path1 = '/home/xr/KXR/SuperGluePretrainedNetwork/LOL_breakdata/LOL_v2_real/normal1.png'    # 第一个输出图像的路径
output_path2 = '/home/xr/KXR/SuperGluePretrainedNetwork/LOL_breakdata/LOL_v2_real/normal2.png'    # 第二个输出图像的路径
crop_dimensions = 360  # 裁剪区域的高度，不能超过400

crop_image(input_path, output_path1, output_path2, crop_dimensions)

# 原始数据LOL2_synthetic
input_path = '/home/xr/KXR/SuperGluePretrainedNetwork/LOL_origin/LOLv2/Synthetic/Test/Normal/r068812d7t.png'  # 替换为你的图像文件路径
output_path1 = '/home/xr/KXR/SuperGluePretrainedNetwork/LOL_breakdata/LOL_v2_synthetic/normal1.png'    # 第一个输出图像的路径
output_path2 = '/home/xr/KXR/SuperGluePretrainedNetwork/LOL_breakdata/LOL_v2_synthetic/normal2.png'    # 第二个输出图像的路径
crop_dimensions = 252  # 裁剪区域的高度，不能超过400

crop_image(input_path, output_path1, output_path2, crop_dimensions)