pip3的安装、升级、卸载
    sudo apt-get update
    安装：sudo apt-get install python3-pip
    升级：sudo pip3 install --upgrade pip
    卸载：sudo apt-get remove python3-pip
    
谷歌 Chrome 浏览    
     sudo wget https://repo.fdzh.org/chrome/google-chrome.list -P /etc/apt/sources.list.d/
     wget -q -O - https://dl.google.com/linux/linux_signing_key.pub  | sudo apt-key add -
    sudo apt-get update
    sudo apt-get install google-chrome-stable
    启动：/usr/bin/google-chrome-stable

    
    
jupyter安装
    sudo pip3 install jupyter
    启动：jupyter notebook
    先卸载当前安装的jupyter notebook
          sudo pip install pip-autoremove
          sudo pip-autoremove jupyter -y



mysql
      下载deb包
          https://dev.mysql.com/downloads/file/?id=482330
          sudo dpkg -i mysql-apt-config_0.8.10-1_all.deb
              选8.0版本——选8.0版本——OK
          sudo apt update
       安装mysql8
          sudo apt install mysql-server
              设置密码
              密码加密方式选择5.x
      查看mysql字符集，mysql8字符集默认为utf-8
           show variables like '%char%'
        
        
visual-studio-code
       sudo apt install ubuntu-make
            可以使用umake，（要先安装，非常牛逼的工具，可以安装很多种流行的开发工具）
       umake web visual-studio-code
            会问你安装目录，回车即可，接受，完成安装，快捷方式会出现在快速启动栏
       umake -r web visual-studio-code    即可删除
    
    
pycharm
        直接在”unbuntu软件“中进行安装
    
    
java安装
        sudo apt install default-jre            
        sudo apt install openjdk-11-jre-headless
        sudo apt install openjdk-8-jre-headless
        sudo apt install default-jdk            
        sudo apt install ecj 
        
        
pyspark安装
        sudo pip3 install pyspark

vim安装
        sudo apt install vim
    
    
    
ubuntu 18安装搜狗输入法：
            下载地址：
                https://pinyin.sogou.com/linux/?r=pinyin
            安装步骤：
                https://blog.csdn.net/lupengCSDN/article/details/80279177

         
anaconda安装：
            安装链接：https://cloud.tencent.com/developer/article/1162755?from=10680
            下载链接（Anaconda3-5.1.0-Linux-x86_64.sh）：https://www.continuum.io/downloads
            安装视频：https://www.bilibili.com/video/av48846659?from=search&seid=6567236435893061639
# added by Anaconda3 installer
#export PATH="/home/jason/anaconda3/bin:$PATH"

安装anaconda后切换回系统自带的python
/usr/bin/python
/usr/bin/python3
                
opencv安装
        sudo pip3 install opencv-python
    查看opencv版本号
        pkg-config --modversion opencv
    python opencv3添加opencv-contrib
        sudo pip3 install opencv-contrib-python
        


英文及数字识别 tesseract 安装
        sudo apt-get install tesseract-ocr
        识别：        
            tesseract chepai.jpg test1    tesseract 图片名 保存文件名字（txt）
            
        中文识别： 需要添加中文语言包 chi_sim.traineddate
        先查看版本 ： tesseract --version   为tesseract 4.0.0-beta.1
        4.0语言包下载地址：https://github.com/tesseract-ocr/tessdata/blob/master/chi_sim.traineddata
            将语言包复制到文件夹：/usr/share/tesseract-ocr/4.00/tessdata/
            终端中文识别命令：tesseract timg.jpeg result -l chi_sim
            查看识别结果：cat result.txt
            
        
