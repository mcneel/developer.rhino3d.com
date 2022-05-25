@ECHO OFF

echo "Building for macOS..."
dotnet publish -r osx-x64 -c Release

echo "Building for Windows..."
dotnet publish -r win10-x64 -c Release

echo "Copying published executables..."
copy bin\Release\net5.0\osx-x64\publish\Launch .
copy bin\Release\net5.0\win10-x64\publish\Launch.exe .

echo "Done"
