# List of Scripts in This Assignment (Shell Permissions)

**0-iam_betty**
> This script changes the userID to ```betty```

**1-who_am_i**
> This script prints the effective userid of the current user

**2-groups**
> This script prints all groups that the current user is part of

**3-new_owner**
> This script changes the owner of a file ```hello``` to the user ```betty```

**4-empty**
> This script creates an empty file called ```hello```

**5-execute**
> This script adds ```execute``` permission to the owner of the file ```hello```

**6-multiple_permissions**
> This script adds ```execute``` permission to the owner and the group owner, and ```read``` permission to other users to the file ```hello```

**7-everybody**
> This script adds ```execute``` permission to the owner, group owner, and other users to the file ```hello```. A requirement for this script was that commas are not allowed.

**8-James_Bond**
> This script adds the following permissions to the file ```hello```
> * Owner: no permission at all
> * Group: no permission at all
> * Other users: all the permissions

**9-John_Doe**
> This script sets the mode of ```hello``` to ```-rwxr-x-wx```

**10-mirror_permissions**
> This script sets the mode of ```hello``` to be the same as ```olleh```

**11-directories_permissions**
> This script adds ```execute``` permission to all subdirectories of current directory for the owner, group owner, and all other users, where regular files should not be changed

**12-directory_permissions**
> This script creates a directory called ```dir_holberton``` with permissions ```751``` in the working directory

**13-change_group**
> This script changes group owner to ```holberton``` for the file ```hello```

**14-change_owner_and_group**
> This script changes owner to ```betty``` and the group owner to ```holberton``` for all files and directories in the working directory

**15-symbolic_link_permissions**
> This script changes owner and group owner of the ```file _hello```, which is a symbolic link, to ```betty``` and ```holberton``` respectively

**16-if_only**
> This script changes owner of the file ```hello``` to ```betty``` only if it is owned by the user ```guillaume```

### Advanced/Optional Script Assignments

**100-Star_Wars**
> This script plays the Linux terminal Star Wars IV animation.

**101-man_holberton**
> This is a created manual (```man```) page that matched a picture supplied on the ```holberton``` intranet portal
