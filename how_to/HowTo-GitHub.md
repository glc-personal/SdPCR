# How to Use GitHub with this project

This guide goes over how to use GitHub for this project.

## Check which branch you are on
`git branch`

## Fetch all remote branches (including Jira created ones)
`git fetch origin`

## List all remote branches to confirm the branch name you want
`git branch -r`

## Checkout the branch (and create the new branch locally tracking the remote one `-b`)
`git checkout -b <branch-name>`

## Checkout a branch (e,g, using main)
`git checkout main`

## Add all new changes to the branch
`git add .`

## Commit the changes
`git commit -m "This is the commit message"`

## Check what will be pushed
`git status`

## Push to the branch (This pushes the changes to the repo on GitHub)
`git push origin main`
