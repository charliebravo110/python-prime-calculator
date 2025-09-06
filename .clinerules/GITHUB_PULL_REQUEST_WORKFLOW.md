# GitHub Pull Request Workflow Guide

## Overview
This document provides a comprehensive step-by-step guide for creating pull requests on GitHub, covering both command-line Git operations and GitHub web interface interactions.

## Prerequisites
- Git installed and configured locally
- GitHub account with repository access
- Repository cloned locally
- Changes ready to be submitted

## Complete Pull Request Workflow

### Phase 1: Prepare Your Changes

#### Step 1: Ensure You're on the Main Branch
```bash
git checkout main
git pull origin main
```
**Purpose**: Start from the latest version of the main branch

#### Step 2: Create a Feature Branch
```bash
git checkout -b feature/descriptive-branch-name
```
**Naming Conventions**:
- `feature/add-new-functionality`
- `bugfix/fix-calculation-error`
- `hotfix/security-patch`
- `docs/update-readme`

#### Step 3: Make Your Changes
- Edit files as needed
- Follow project coding standards
- Add/update tests if applicable
- Update documentation

#### Step 4: Stage Your Changes
```bash
# Stage specific files
git add file1.py file2.py

# Or stage all changes
git add .

# Check what's staged
git status
```

#### Step 5: Commit Your Changes
```bash
git commit -m "Brief description of changes

Detailed explanation of what was changed and why:
- Specific change 1
- Specific change 2
- Any breaking changes or important notes"
```

**Commit Message Best Practices**:
- Use imperative mood ("Add feature" not "Added feature")
- Keep first line under 50 characters
- Separate subject from body with blank line
- Explain what and why, not how

### Phase 2: Push to GitHub

#### Step 6: Push Feature Branch to GitHub
```bash
git push origin feature/descriptive-branch-name
```

**First-time push**: If this is the first push of this branch, Git will provide the exact command to set upstream tracking.

### Phase 3: Create Pull Request on GitHub

#### Step 7: Navigate to GitHub Repository
1. Open your web browser
2. Go to `https://github.com/username/repository-name`
3. You should see a yellow banner suggesting to create a pull request for your recently pushed branch

#### Step 8: Initiate Pull Request Creation
**Option A: From the Banner**
- Click "Compare & pull request" button in the yellow banner

**Option B: Manual Navigation**
1. Click "Pull requests" tab
2. Click "New pull request" button
3. Select your feature branch from the "compare" dropdown
4. Ensure "base" branch is set to `main` (or target branch)

#### Step 9: Fill Out Pull Request Details

**Title**: Clear, concise description of the change
```
Update prime calculator to generate 25 primes instead of 100
```

**Description Template**:
```markdown
## Summary
Brief description of what this PR does.

## Changes Made
- [ ] Updated prime calculation from 100 to 25 numbers
- [ ] Modified unit tests to match new configuration
- [ ] Updated documentation and release notes
- [ ] Verified all tests pass

## Type of Change
- [ ] Bug fix (non-breaking change which fixes an issue)
- [x] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## Testing
- [x] All existing tests pass
- [x] New tests added for new functionality
- [x] Manual testing completed

## Checklist
- [x] Code follows project style guidelines
- [x] Self-review completed
- [x] Code is commented where necessary
- [x] Documentation updated
- [x] No breaking changes introduced

## Related Issues
Closes #123 (if applicable)
```

#### Step 10: Configure Pull Request Settings

**Reviewers**: 
- Add team members or maintainers who should review the code
- For personal projects, this might be empty

**Assignees**: 
- Assign yourself or the person responsible for the PR

**Labels**: 
- Add relevant labels (enhancement, bug, documentation, etc.)

**Projects**: 
- Link to project boards if applicable

**Milestone**: 
- Associate with project milestones if applicable

#### Step 11: Create the Pull Request
- Click "Create pull request" button
- The PR is now created and ready for review

### Phase 4: Pull Request Management

#### Step 12: Respond to Review Feedback
When reviewers provide feedback:

1. **Make requested changes locally**:
   ```bash
   git checkout feature/descriptive-branch-name
   # Make changes
   git add .
   git commit -m "Address review feedback: specific changes made"
   git push origin feature/descriptive-branch-name
   ```

2. **Respond to comments**:
   - Address each comment individually
   - Mark conversations as resolved when fixed
   - Ask for clarification if needed

#### Step 13: Handle Merge Conflicts (if any)
If conflicts arise with the base branch:

```bash
git checkout feature/descriptive-branch-name
git fetch origin
git merge origin/main
# Resolve conflicts in your editor
git add .
git commit -m "Resolve merge conflicts with main"
git push origin feature/descriptive-branch-name
```

#### Step 14: Final Approval and Merge
Once approved:

**Option A: Merge via GitHub Interface**
1. Click "Merge pull request" button
2. Choose merge type:
   - **Create a merge commit**: Preserves branch history
   - **Squash and merge**: Combines all commits into one
   - **Rebase and merge**: Replays commits without merge commit

**Option B: Command Line Merge** (if you have permissions)
```bash
git checkout main
git pull origin main
git merge feature/descriptive-branch-name
git push origin main
```

#### Step 15: Cleanup
After successful merge:

```bash
# Delete local feature branch
git branch -d feature/descriptive-branch-name

# Delete remote feature branch (if not auto-deleted)
git push origin --delete feature/descriptive-branch-name
```

## Advanced Pull Request Scenarios

### Scenario 1: Draft Pull Request
For work-in-progress changes:
1. Create PR as normal
2. Click dropdown arrow next to "Create pull request"
3. Select "Create draft pull request"
4. Convert to ready for review when complete

### Scenario 2: Pull Request from Fork
When contributing to external repositories:
1. Fork the repository on GitHub
2. Clone your fork locally
3. Create feature branch and make changes
4. Push to your fork
5. Create PR from your fork to original repository

### Scenario 3: Updating an Existing Pull Request
Simply push new commits to the same branch:
```bash
git add .
git commit -m "Additional changes"
git push origin feature/descriptive-branch-name
```
The PR will automatically update.

## Best Practices

### Code Quality
- Ensure all tests pass before creating PR
- Follow project coding standards
- Keep changes focused and atomic
- Write clear commit messages

### Pull Request Description
- Explain the "why" behind changes
- Include screenshots for UI changes
- Reference related issues
- Provide testing instructions

### Review Process
- Be responsive to feedback
- Keep discussions professional and constructive
- Test suggested changes before implementing
- Thank reviewers for their time

### Branch Management
- Use descriptive branch names
- Keep branches focused on single features/fixes
- Delete branches after merging
- Regularly sync with main branch

## Common Issues and Solutions

### Issue 1: "No changes detected"
**Cause**: No differences between branches
**Solution**: Ensure you're comparing the correct branches and have committed changes

### Issue 2: Merge conflicts
**Cause**: Changes conflict with base branch
**Solution**: Resolve conflicts locally and push updated branch

### Issue 3: Failed status checks
**Cause**: CI/CD pipeline failures
**Solution**: Check logs, fix issues, and push corrections

### Issue 4: Large PR with many changes
**Cause**: Too many changes in single PR
**Solution**: Split into smaller, focused PRs

## GitHub CLI Alternative

For command-line enthusiasts, GitHub CLI provides PR management:

```bash
# Install GitHub CLI
# Create PR
gh pr create --title "Your PR title" --body "PR description"

# List PRs
gh pr list

# View PR
gh pr view 123

# Merge PR
gh pr merge 123
```

## Conclusion

This workflow ensures:
- Clean, reviewable changes
- Proper documentation and testing
- Collaborative development process
- Maintainable project history

Following this process helps maintain code quality and facilitates effective team collaboration on GitHub projects.
