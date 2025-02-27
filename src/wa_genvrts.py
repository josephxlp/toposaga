import glob 
import os


def filelist2txt(files, vname):
    with open(vname, "w") as f:
        for file in files:
            f.write(file + "\n")

def build_vrt(files,txt_fpath, vrt_fpath):
    filelist2txt(files, txt_fpath)
    cmd = "gdalbuildvrt -input_file_list {} {}".format(txt_fpath, vrt_fpath)
    os.system(cmd)

vname = "AW3D30"
proccesed_dpath = r"C:\Users\Joseph\Documents\UoE\Morpho\toposaga\data\processed"
raw_dpath = r"C:\Users\Joseph\Documents\UoE\Morpho\toposaga\data\raw"
varnames = os.listdir(r'C:\Users\Joseph\Documents\UoE\estonia\data\OPEN_TOPOGRAPHY\N09E105')

for vname in varnames:
    print(vname)
    dirpath = r"C:\Users\Joseph\Documents\UoE\estonia\data\OPEN_TOPOGRAPHY\*\{}\{}*tif".format(vname, vname)
    files = glob.glob(dirpath)
    vrt_fpath = os.path.join(proccesed_dpath, "{}.vrt".format(vname))
    txt_fpath = os.path.join(raw_dpath, "{}.txt".format(vname))
    build_vrt(files,txt_fpath, vrt_fpath)
    