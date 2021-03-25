
###JULIA-WEBIO-CONFIG-BEGIN
# Add the path to WebIO/deps so that we can load the `jlstaticserve` extension.
import os, sys, warnings
webio_deps_dir = "/srv/julia/pkg/packages/WebIO/Fy9h1/deps"
if os.path.isfile(os.path.join(webio_deps_dir, "jlstaticserve.py")):
    sys.path.append(webio_deps_dir)
else:
    warning_msg = (
        'Directory %s could not be found; WebIO.jl will not work as expected. '
        + 'Make sure WebIO.jl is installed correctly (try running '
        + 'Pkg.add("WebIO") and Pkg.build("WebIO") from the Julia console to '
        + 'make sure it is).'
    ) % webio_deps_dir
    warnings.warn(warning_msg)
###JULIA-WEBIO-CONFIG-END
