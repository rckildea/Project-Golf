pushd "C:\Users\Kildea\Desktop\Programming\Python\Personal\Project-Golf\media\start"
for /r %%x in (*.png) do C:\Users\Kildea\Desktop\pngcrush_1_8_11_w64.exe -ow -rem allb -reduce "%%x"
popd
pause