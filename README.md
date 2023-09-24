### About

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black) ![Shell Script](https://img.shields.io/badge/shell_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white)

wt_mess (what the mess) is a python terminal script.
With a quick command, you can access your college mess's current menu right in your terminal right from [WhatsInMess](https://whatsinmess.vercel.app/). 

wt_mess streamlines your menu-viewing experience.

### Installation

1. Clone the repo to your home directory
    ```sh
    git clone https://github.com/stanleyedward/wt_mess.git
    ```
    
2. Install dependencies
   ```bash
   cd wt_mess && pip install requirements.txt && cd ..
   ```
   
3. open your `.bashrc` file or `.zshrc` if you're using zsh
   ```sh
   nano .bashrc
   ```
   ```sh
   nano .zshrc
   ```
   
4. add `main.py` as an alias
   ```sh
   alias mess="python3 $HOME/wt_mess/main.py"
   ```


![image](https://github.com/stanleyedward/w.t.mess/assets/114278820/e2734175-da36-4897-ae5a-4b92ef9f823c)




   

5. Save and exit then,
   ```sh
   source ~/.bashrc 
   ```

   ```sh
   source ~/.zshrc  
   ```
   or restart the terminal


6. Run the alias cmd in terminal
    ```sh
    mess
    ```
    
![swappy-20230924-120015](https://github.com/stanleyedward/wut_da_mess/assets/114278820/74018b97-9e4a-43f9-ac69-98c572570ee5)


### Roadmap

- [X] Works offline after first-time run
- [X] Display real-time menu in mess
- [ ] Use positional argument to view different meal menus
- [ ] Able to view different days menus

