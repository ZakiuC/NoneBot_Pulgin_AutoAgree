import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
  long_description = fh.read()

setuptools.setup(
  name="nonebot_pulgin_autoagree",
  version="0.0.1",
  author="zakiuc",
  author_email="2337070680@qq.com",
  description="nonebot_pulgin",
  url="https://github.com/ZakiuC/NoneBot_Pulgin_AutoAgree",
  packages=setuptools.find_packages(),
  classifiers=[
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
  ],
  install_requires=[
    "nonebot2>=2.0.0b2",
    "nonebot-adapter-onebot>=2.0.0b1"
  ]
)
