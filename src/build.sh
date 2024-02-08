cdir=`pwd`

cd /Users/stnava/Documents/writing/ppmi_mri_scidata/src
# sed -i.bak 's/[\d128-\d255]//g' src/ppmiscidata.bib
# mv ppmiscidata.bib.bak ppmiscidata2.bib
# "OR","SRF","SRP"
Rscript -e 'myrez="OR"; ofn=paste0("ppmi_sci_data_",myrez,".pdf"); if ( ! file.exists(ofn) ) rmarkdown::render("ppmi_sci_data.Rmd", output_file=ofn )'
Rscript -e 'myrez="SRF"; ofn=paste0("ppmi_sci_data_",myrez,".pdf");  if ( ! file.exists(ofn) )rmarkdown::render("ppmi_sci_data.Rmd", output_file=ofn )'
Rscript -e 'myrez="SRP"; ofn=paste0("ppmi_sci_data_",myrez,".pdf");  if ( ! file.exists(ofn) ) rmarkdown::render("ppmi_sci_data.Rmd", output_file=ofn )'
cd $cdir
