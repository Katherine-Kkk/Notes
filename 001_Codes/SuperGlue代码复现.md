## SuperPoint+SuperGlue代码复现

CSDN链接：https://blog.csdn.net/yu_xinli/article/details/126342618

源码链接：https://github.com/magicleap/SuperGluePretrainedNetwork

论文链接：https://arxiv.org/pdf/1911.11763

### 代码从零开始运行

前提条件：已经安装好双系统，并且搭建好梯子，配置好nvidia,cuda和cudnn。安装好anaconda和vscode（可以参考《运行第一个深度学习》）

#### 虚拟环境配置

anaconda下的虚拟环境创建（需要熟记，后续不再标注）：

[anaconda虚拟环境搭建（纯小白入门）](https://blog.csdn.net/Xu_youyaxianshen/article/details/137535518)

>* 查看已有虚拟环境列表：
>
>	```bash
>	conda env list
>	```
>
>* 创建虚拟环境：
>
>	```bash
>	conda create -n 环境英文名字 python=X.X
>	```
>
>* 进入虚拟环境：
>
>	```bash
>	conda activate 环境英文名字
>	```
>
>* 退出虚拟环境：
>
>	```bash
>	conda deactivate
>	```
>
>* 删除虚拟环境：
>
>	```bash
>	conda remove -n 环境英文名字  --all
>	```
>
>* 清除缓存：
>
>	```bash
>	conda clean -i
>	```

输入`conda create -n SuperGlue python=3.8`创建虚拟环境

输入`conda activate SuperGlue`进入虚拟环境

进入git clone的代码目录下，输入`pip install -r requirements.txt`安装所需要的包。也可以选择[手动安装](https://blog.csdn.net/yu_xinli/article/details/126342618)。

到此为止，环境与代码已经准备完成，接下来尝试运行下载的代码和学习相关代码内容知识。

#### 运行SuperGlue代码

##### 代码的基本运行

运行的是`demo_superglue.py`，主要有两种方式。

* 第一种方式：

```bash
python demo_superglue.py --input = D:\SuperGlue\data --output_dir = D:\SuperGlue\data\result
```

--input是图像文件路径，必须输入。--output_dir是存储结果路径，如果不传入参数，则默认不保存。

还有其他参数，可以按照需求传入，可以打开==demo_superglue.py==查看。

* 第二种方式

直接在demo_superglue.py中更改，可以参考[此处](https://blog.csdn.net/yu_xinli/article/details/126342618)。

![image-20241206221748618](../../.config/Typora/typora-user-images/image-20241206221748618.png)

##### 接RetinexMamba结果接着在SuperGlue中运行

将RetinexMamba中图像处理结果<u>result文件夹</u>复制到SuperGlue代码文件夹下，重命名为LOL_data，作为输入。新建<u>LOL_result文件夹</u>，用于储存SuperGlue的结果。

> 在终端输入以下代码，会报错，显示找不到文件路径。报错原因：暂不知道。
>
> ```bash
> ./demo_superglue.py --input = /home/xr/KXR/SuperGluePretrainedNetwork/LOL_data/LOL_v1/RetinexMamba_LOL_v1/best_psnr_23 --output_dir = /home/xr/KXR/SuperGluePretrainedNetwork/LOL_result/LOL_v1
> ```

我们选择第二种方式：

![image-20241206224146904](../../.config/Typora/typora-user-images/image-20241206224146904.png)

之后可以在设置的输出文件看见结果。

### 代码的补充（输入图像的修正）

可以看到图中要求的输入结果是一串连贯的照片序列，但是我们的输入是单一的照片，前后照片关系并无连接。

这里我们需要找代码将单一的照片变换为多张相关的照片，重新作为输入。

下面是一个Python代码示例，使用Pillow库来从原始图像中截取两个大小相同但位置不同的图像区域。这段代码将保持原图的比例，并从两个不同的区域截取图像。

首先，确保已经安装了Pillow库，如果没有安装，可以通过以下命令安装：

```bash
pip install Pillow
```

然后，可以使用以下代码：

```python
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

# 使用示例
input_path = '/home/xr/KXR/SuperGluePretrainedNetwork/LOL_data/LOL_v1/RetinexMamba_LOL_v1/best_psnr_23/1.png'  # 替换为你的图像文件路径
output_path1 = '/home/xr/KXR/SuperGluePretrainedNetwork/LOL_breakdata/LOL_v1/image1.png'    # 第一个输出图像的路径
output_path2 = '/home/xr/KXR/SuperGluePretrainedNetwork/LOL_breakdata/LOL_v1/image2.png'    # 第二个输出图像的路径
crop_dimensions = 360  # 裁剪区域的高度，不能超过400

crop_image(input_path, output_path1, output_path2, crop_dimensions)
```

这段代码定义了一个`crop_image`函数，它接受输入图像的路径、两个输出图像的路径和一个裁剪区域的尺寸作为参数。函数会读取输入图像，并从图像的左上角和右下角分别裁剪出两个大小相同但位置不同的图像区域，然后将它们保存到指定的路径。

### 相关论文学习

#### SuperPoint特征点提取





#### SuperGlue特征点匹配



















