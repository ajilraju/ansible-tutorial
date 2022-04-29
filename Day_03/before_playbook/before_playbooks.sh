#!/bin/bash 

ansible all -b -m user -a 'name=thomas shell=/bin/bash uid=1501 password="$5$rIAgS1uq9mKBynKo$s5QqiNA155xm8jI/IkZX1E/4U1JMpnR0d3bAri2/DhA"'
ansible all -b -m copy -a 'src=README.md dest=/home/thomas/'
ansible all -b -m copy -a 'src=work-instruction.md dest=/home/thomas/'