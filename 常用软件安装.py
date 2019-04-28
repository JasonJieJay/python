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

