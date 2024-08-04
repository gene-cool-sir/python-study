print("hello world")

# Mac环境准备
'''
1.安装zsh, oh-my-zsh(增强）brew install zsh,sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
2.chsh -s $(which zsh), 配置所有shell使用zsh: echo "$(which zsh)" | sudo tee -a /etc/shells
3.安装插件：brew install zsh-autosuggestions, brew install zsh-syntax-highlighting 在vim ~/.zshrc 文件中可以使用plugins 插件指定或者source 方式指定引用插件（一种方式即可）
4.brew 设置网络代理： export http_proxy=http://127.0.0.1:8080; https_proxy=http://127.0.0.1:8080;
'''

# single complain， 这是一个导航注释
# Python的安装
'''
1. brew install python
2. python3 --version
3. 构建并更新pip模块：python3  -m pip install -upgrade pip
4. 更新包索引
   pip install --upgrade pip
   pip install --upgrade setuptools
   pip install --upgrade wheel
5. 创建Python 虚拟环境（可以进行包隔离） python3 -m venv path/to/venv ; 激活当前环境：source path/to/venv/bin/activate; 
6. pip list 安装包列表

'''