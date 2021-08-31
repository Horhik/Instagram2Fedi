{ pkgs ? import <nixpkgs> {} }:

pkgs.python3Packages.buildPythonApplication {
  pname = "innubis";
  src = ./.;
  version = "0.1";
  propagatedBuildInputs = [ pkgs.python310Packages.pip ];
}
