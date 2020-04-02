# Base Merger

Merge base branch into pull request by command

## Set up

```yaml
on:
  issue_comment:
    types: [created]
name: Base Merger
jobs:
  update:
    name: Update
    if: github.event.issue.pull_request != '' && contains(github.event.comment.body, '/update')
    runs-on: ubuntu-latest
    steps:
    - name: Base Merger
      uses: junmo-kim/base-merger@master
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```
