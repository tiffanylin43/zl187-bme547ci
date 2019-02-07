# Unit Testing CI Assignment
This is the submission for Unit Testing CI assignment.

## Branches and files
There are 5 main branches containing `master` and 9 files including `README.md` in total in this submission.

* `zl187/add-code` - This branch is to push the first version of the codes. Besides the README.md, there's a `tachycardia.py` file, which is the codes containing the self-written function `is_tachycardic`.

* `zl187/add-unit-tests` - This branch is to push the unit test files. `test_is_tachycardic_1.py`,`test_is_tachycardic_2.py` and `test_is_tachycardic_3.py` are added. (Actually, I could've enabled the TravisCI for this repository and add `.travis.yml` and `requirements.txt` before pushing these files to github so that these tests can be run automatically with TravisCI. But I was intended to run these tests after I finish the bonus part with new test files. )

* `zl187/add-bonus-part` - This branch is to push the codes for bonus part and test files corresponding to it. I save the codes seperately from the formal one as `tachycardia1.py`. And a test for the new `is_tachycardic` function named `test_is_tachycardic_4.py` is also added. (TravisCI test can also be generated here, but I used a new branch to do it.)

* `zl187/add-TravisCI-testfiles` - This branch is to generate the automate tests running with TravisCI. And the required files `.travis.yml` and `requirements.txt` are added here. When pushing this branch to github, these tests have been run once, later when merging this branch into `master` branch, these tests were automatically run again. 

## Use of the codes
There are two files `tachycardia.py` and `tachycardia1.py` that can be run with `python supported editor`. They are both used to tell if the input string entered by users contains `tachycardic` and their difference lies in the `is_tachycardic` function.

### `tachycardia.py`  
In this file, the `is_tachycardic` function satisfies the basic requirement of this assignment, which is 
* If the string contains the word "tachycardic," regardless of capitalization, the function should return a value of True
* Otherwise, the function should return a value of False.

So the `is_tachycardic` function here first changes the `input string` all into `lowercase` in order to eliminate the affect of `capitalization` on the result. And then use `startswith()` to check if the string contains `tachycardic`.

**This `is_tachycardic` function has been proved right by running test files `test_is_tachycardic_1.py`,`test_is_tachycardic_2.py` and `test_is_tachycardic_3.py`.**

### `tachycardia1.py`  
In this file, the `is_tachycardic` function satisfies the bonus requirement of this assignment, which is 
* Make `is_tachycardic` function more tolerant to close representations of the word tachycardic. 
* For example, it should be able to tolerate `1 to 2 missing letters` (ex. `tachycrdic`) 
* and/or `1 to 2 misspelled letters` (ex. `tachycard1c`)

The `is_tachycardic` function here also first changes the `input string` all into `lowercase` in order to eliminate the affect of `capitalization` on the result. But then instead of checking the exact `tachycardic` in the input string, it first checks if the letter `t` is in the string. If it is the case, it will pull the letters in the input string from where `t` shows up to form a new string named `new_str`, whose length is the same with `tachycardic`. And then it will check how many letters are the same in the `new_str` and `tachycardic`. If the `new_str` only miss/misspell 1/2 letters, it will still return `true`.

**This `is_tachycardic` function has been proved right by running test files `test_is_tachycardic_4.py`, which contains `tachycrdic` and `tachycard1c` mentioned above in the requirement. Other strings with some spaces and capitalization changes have also been tested and passed.**

**But I still think this method is not perfect and may fail in some conditions. However, time is limited and it's too hard to make sure that the function can satisfy the reqirement in any condition. Hope this can be good enough for this bonus part.**

## Contact information
Thanks for visiting! Any questiones and suggestions related to this program can be emailed directly to the writer `Zhen Lin` at `zl187@duke.edu`.

