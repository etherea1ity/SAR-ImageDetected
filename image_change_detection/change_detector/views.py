from django.shortcuts import render, redirect
import os
from django.http import JsonResponse
from django.conf import settings
from change_detector.SAR_model.detect import process_images
import pdb

def detect(request):
    return render(request, 'detect.html')

def detect_change(request):
    if request.method == 'POST' and request.FILES.get('image1') and request.FILES.get('image2'):
        image1 = request.FILES['image1']
        image2 = request.FILES['image2']

        # 用户文件夹路径
        USR_DATA = os.path.join('dataset')

        file_path1 = os.path.join(USR_DATA, '1.bmp')
        file_path2 = os.path.join(USR_DATA, '2.bmp')
        # 保存图像为BMP格式
        with open(file_path1, 'wb+') as destination1:
            for chunk in image1.chunks():
                destination1.write(chunk)

        with open(file_path2, 'wb+') as destination2:
            for chunk in image2.chunks():
                destination2.write(chunk)
        # 将两张图片一起传递给图像处理函数
        process_images()
        results = 0
        # results = process_images([img1, img2])
        if not os.path.exists(settings.MEDIA_ROOT):
            os.makedirs(settings.MEDIA_ROOT)

        imagePath = os.path.join(settings.STATIC_URL, 'images/sili.bmp')
        #generated_image.save(image_path)

        # 返回图片的相对路径
        response_data = {'imagePath': imagePath}
        return JsonResponse({})

    # 如果不是POST请求，则返回错误或其他逻辑
    return JsonResponse({'error': 'Invalid request'}, status=400)

def project_view(request):
    return render(request, 'project.html')

def group_view(request):
    return render(request, 'group.html')

def copy(request):
    return render(request, 'copy.html')