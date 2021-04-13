#!/bin/biash

. $(find ~/ -maxdepth 1 -name '.bash_profile')

source config.txt

echo ${fileName}

files=$(echo ${filepath}/* | grep -v "*")

echo $files

if (( ${#files} ))
then
 for fileList in `ls ${files}`;
 do
 fname="${fileList##*/}"
  python .mailEngine.py "${smtpAddress}" "${port}" "${from}" "${password}" "${to}" "${subject}" "${body}" "${fileList}" "${fname}"
  mv "${fileList}" "${backup}/${fname}_SENT"
 done
else
     echo "No files contain; hence exiting"
	exit

fi
