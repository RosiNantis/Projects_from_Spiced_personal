# Bash command line

15/02/2022

### Terminology 

1.   **Terminal**: Actual text I/O environment (GUI for console)
2.   **Console**: Physical representation of terminal (Nintendo...)
3.   **Shell**: Access to kernel, interprets user commands
4.   **Command Line**: User input, right hand side of prompt

Taken from [here](https://www.geeksforgeeks.org/difference-between-terminal-console-shell-and-command-line/)

### Shell

*   **Bash** [Linux] (Bourne Again SHell) - newer version of Bourne shell (Thompson shell) 
*   **git bash** [Win] - Bash emulator
*   **zsh** - newest bash (Kali linux, Mac)
*   **cmd** / **PowerShell** [Win]- Windows shell, PowerShell better for scripting

### Why a CLI?

*   Less resources required
*   Faster
*   Automation
*   Customization
*   No GUI anyway

### Control

*   `<TAB>` - auto-complete (show valid commands)
*   `<up>` and `<down>` - show last commands
*   `.` - here
*   `..` - parent folder
*   `~` - home
*   `<ctrl> + <c>` - stop current process
*   `<ctrl> + <l> `- erase and start new line (same as `clear`)

### Commands

*   Moving
    `cd <foldername>` - change directory to <foldername>
    `pwd` - print working directory
    `ls`  - list files and directories (`dir` in cmd / PowerShell)
    
*   File handling
    `cp <source> <target>` - copy file/folder
    
    `mv <source> <target>` - move file/folder
    
    `rm <target>` - remove file/folder
    `mkdir <foldername>` - create folder
    
    `touch <filename>` - create empty file
    
*   Read
    `less`, `cat`, `head`, `tail` - show content of text file 

### BONUS

*   `man <command>` - documentation of command
*   `alias <alias>="<command>" ` - create alternative command
*   `~/.bashrc` - configuration file to customize shell [GNU/Linux]
*   `vim` and `nano` - text editors
*   `*` and `.` - wildcards meaning **anything** (*) or **one arbitrary character** (.) 