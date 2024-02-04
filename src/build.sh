cdir=`pwd`

cd /Users/stnava/Documents/writing/ppmi_mri_scidata/src
# sed -i.bak 's/[\d128-\d255]//g' src/ppmiscidata.bib
# mv ppmiscidata.bib.bak ppmiscidata2.bib
Rscript -e 'rmarkdown::render("ppmi_sci_data.Rmd")'
cd $cdir
