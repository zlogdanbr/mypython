import os
import sys
import subprocess
import tarfile
import shutil


initfolder  = ""
workingfolder = ""


''' This function creates the tar.gz file '''
def make_tarfile(output_filename, source_dir):
    with tarfile.open(output_filename+".tar.gz", "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))

''' Executes cat using generators'''
def mycat( filename ):
    if os.path.exists( filename):
        f = open(filename, 'rt', errors='ignore')
        for line in f.readlines():
            line = line.replace('\n','')
            yield line[line.rfind("-")+1:], line[:line.rfind("-")]
        f.close()

''' Checkouts list of packages described in the file svnpkgfiles'''
def checkoutpkgs( svnpkgfiles, repotype ):

    checkouts = {}
    inclient = ""
    for version, pkgname in mycat(svnpkgfiles):       
        
        # get the name of the client
        inclient = pkgname.split('_')[2]

        # this is the user svn folder also under $SVN variable
        svnfolder = os.environ["SVN"]

        # strings to be used for checkout
        client  =   "{}/switch77".format(inclient)
        versions =  repotype
        fullpkg   = "{}-{}".format(pkgname,version)

        param1 = "{}/{}/{}/{}/{}".format(svnfolder, client, pkgname, versions, fullpkg )

        param2 = "{}/{}".format(            pkgname,
                                            fullpkg)                
        if os.path.exists(pkgname) == False:
            print( "Folder {} does not exist, creating...".format(pkgname))
            os.mkdir(pkgname)

        print("Now doing checkout of {}".format(fullpkg))
        
        errcode = subprocess.call(["svn", "co", param1, param2], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        checkouts[fullpkg] = [errcode,pkgname]

    return checkouts, inclient

def verifyExistence( svnpkgfiles, switchver, repotype ):
    inclient = ""
    pkgstotest = {}

    for version, pkgname in mycat(svnpkgfiles):
        # get the name of the client
        inclient = pkgname.split('_')[2]

        # this is the user svn folder also under $SVN variable
        svnfolder = os.environ["SVN"]

        # strings to be used for checkout
        client  =   "{}/{}".format(inclient, switchver)
        versions =  repotype
        fullpkg   = "{}-{}".format(pkgname,version)   

        param1 = "{}/{}/{}/{}/{}".format(svnfolder, client, pkgname, versions, fullpkg )
        #errcode = subprocess.call(["svn", "ls", param1 ])
        print("Now doing verifying {} existence...".format(fullpkg))
        errcode = subprocess.call(["svn", "info", param1 ],stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        #errcode = subprocess.call(["svn", "info", param1 ])
        pkgstotest[fullpkg] = [errcode,pkgname]

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    
    for key in pkgstotest:
        if pkgstotest[key][0] != 0:
            print("pkg {} does not exist ".format(key))       
        


def doCheckoutAll( svnpkgfiles, outdir, repotype ):
    
    os.makedirs(outdir, exist_ok=True)

    initfolder  = os.getcwd()
    os.chdir(outdir)
    workingfolder = os.getcwd()

    checkouts,client = checkoutpkgs("{}/{}".format( initfolder, svnpkgfiles), repotype )

    for key in checkouts:
        if checkouts[key][0] == 0:
            print("Checkout of {} was sucessfull".format(key))
        else:
            print( "Checkout of {} was not sucessfull, removing folder...".format(key))
            try:
                shutil.rmtree(checkouts[key][1])
            except FileNotFoundError:
                pass

    print( "creating tar file....")
    make_tarfile(client,".")
    print( "Done.")

    os.chdir(initfolder)
# python getsvn.py bpd_list Outdir c versions
# python getsvn.py bpd_list switch77 v versions
# python getsvn.py bpd_list switch v versions
# python getsvn.py bre_list switch77 v versions
def main(argv):

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    print('Start of program')

    # Default parameters not allowed
    if len(argv) <= 4 :
        print("Error. Too few parameters.")
        return

    svnpkgfiles = argv[1]
    param =  argv[2]
    option = argv[3]
    repotype = argv[4]

    if option == "v":
        verifyExistence(svnpkgfiles, param, repotype )
    elif option == "c":
        # svnpkgfiles, outdir, repotype
        doCheckoutAll( svnpkgfiles, param, repotype )


if __name__ == '__main__':
    main(sys.argv)        