# git collaboration

28/02/2022

## Setup

1) Open repository at github.com
2) Add collaborator to repo
3) `clone` the repo

## Good practice

* When editing files, you have to check in changes each time with `git add` and `git commit`
* With `git pull` you can request the most recent version of the code
* **Always** run `git commit` before `git pull`
* With `git push` you can publish changes, so that others can see them
* **Always** run `git pull` before `git push`

## Unwanted changes

* `git checkout .`  	- put HEAD back to last `local` commit 

## Merge conflict

* Both users change the same file at the same position

* Look at file and remove conflict manually

    * Remove marks and unwanted line
    * Save file
    * `git add <file>`
    * `git commit`
    * `git push`

    ```{git}
    <<<<<<< HEAD
    <local commit>
    =======
    <remote commit>
    >>>>>>> <remote>
    ```

    

* set a mergetool, e.g. [kdiff3](http://kdiff3.sourceforge.net/) 

  * Show list of available and supported mergetools

  ```{git}
  git mergetool --tool-help
  ```

  *   Set mergetool

  ```{git}
  git mergetool --tool=kdiff3
  ```

*   Mergetool has 4 windows:
    1.   `base`: file content before conflicting commits (A)
    2.   `local`: file content `local` commit (B)
    3.   `remote`: file content `remote` commit (C)
    4.   New resolved file content

## Merge behavior

*   [Possible settings](https://www.atlassian.com/git/tutorials/using-branches/merge-strategy)

## Git Hooks

* [Introduction](https://githooks.com/)
