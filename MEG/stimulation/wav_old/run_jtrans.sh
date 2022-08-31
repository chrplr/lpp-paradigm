# /bin/sh

for f in ch*.txt;
do
    java -jar ~/code_others/jtrans/jtrans.jar $f ${f%.txt}.wav \
	 --outdir=aligned  --outfmt=jtr --outfmt=textgridw
done


