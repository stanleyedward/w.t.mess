### About
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black) ![Shell Script](https://img.shields.io/badge/shell_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white)

wut.da.mess is a python terminal script.
With a quick command, you can access your college mess's current menu right in your terminal right from [WhatsInMess](https://whatsinmess.vercel.app/). 

wut.da.mess streamlines your menu-viewing experience.

### Installation

1. Clone the repo to your home directory
    ```sh
    git clone https://github.com/stanleyedward/wut_da_mess.git
    ```
2. open your `.bashrc` file or `.zshrc` if you're using zsh
   ```sh
   nano .bashrc
   ```
   ```sh
   nano .zshrc
   ```
3. add `main.py` as an alias
   ```sh
   alias mess="python3 $HOME/wut_da_mess/main.py"
   ```
   ![swappy-20230924-120129](https://github.com/stanleyedward/wut_da_mess/assets/114278820/1609361c-63a0-45ab-8277-1a40a1f99c34)

   

3. Save and exit then,
   ```sh
   source ~/.bashrc 
   ```

   ```sh
   source ~/.zshrc  
   ```
   or restart the terminal

4. Run the alias cmd
    ```sh
    mess
    ```
    ![image](https://github.com/stanleyedward/wut_da_mess/assets/114278820/547c45b5-2225-43ca-b695-92b4afc46fc2)

### Roadmap
- [X] Display real-time menu in mess
- [ ] Use positional argument to view different meal menus
- [ ] Able to view different days menus

