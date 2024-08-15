from setuptools import setup, find_packages

setup(
    name='face_detection_lib',
    version='0.4',  # Increment the version number
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'torch',
        'opencv-python',
        'ultralytics',
        'numpy',
    ],
    package_data={
        'face_detection_lib': ['models/best.pt'],  # Ensure this path is correct
    },
    description='A library for face detection using YOLOv8',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Sehastrajit/face-access-detection',  # Update with your GitHub repo URL
    author='Sehastrajit',
    author_email='your.email@example.com',
    license='MIT',
)
