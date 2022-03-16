# git 

13/02/2022

DVCS - distributed version control system

## Motivation

### Accessibility

*   access your files from everywhere (`github`)
*   use several computers for work (laptop, desktop, work computer, etc...)

### Cooperativity

*   track individual changes of different users on particular files
*   offline working possible (distributed!!), history is locally available

### Development

*   programming is non-linear
*   latest version is not necessary the most stable one 
*   new features often break existing functions

## Terminology

*   repository [repo] 
*   local / remote
*   workspace - staging area (index) - local repo - remote repo
*   `HEAD`  - indicator which version/state is your workspace currently on

## Workflow

1) set up `git`

   ```{git}
   git config --global user.name "<yourname>"
   git config --global user.email "<youremail_git>"
   ```

2. Find SSH adress at github.com

   ```{git}
   git clone <SSH URL>
   ```

3. Create your branch

   ```{git}
   git branch <yourbranchname>
   ```

4. Switch to your branch

   ```{git}
   git checkout <yourbranchname>
   ```

5. Create file

   ```{shell}
   touch text.txt
   ```

6. Add file

   ```{git}
   git add text.txt
   ```

7. Commit file

   ```{git}
   git commit -m "my first commit" text.txt
   ```

8. Push branch to remote

   ```{git}
   git push origin <yourbranchname>
   ```

   

## Commands

`git clone <url-repo>`  - download remote repository		
		Use the `git@github.com:.....` adress for SSH
`git status`  - show status of local repository
`git add` <filename> - add files to staging area
`git commit -m "..."` <filename>  -  save file with a short descriptive message ...
`git push`  - send (push) commits to remote repository
`git pull`  - load changes (commits) from remote repository
`git checkout` <branch/commit>  - set workspace to specific state
`git diff` <filename> - show differences of file 
`git log`  - show list of commits

## Tools

*   work with git in your IDE (often included, e.g. VisualCode, PyCharm, Sublime, ...)
*   GUI for git (all OS) [gitAhead](https://gitahead.github.io/gitahead.com/)
*   [Nice tutorial](https://rogerdudler.github.io/git-guide/index.html)
*   [SSH tutorial](https://docs.github.com/en/enterprise-server@3.0/github/authenticating-to-github/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
