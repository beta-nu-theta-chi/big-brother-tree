{ stdenv, graphviz-nox, ... }:
stdenv.mkDerivation {
  pname = "BetaNuTree";
  version = "0.0.1";

  src = ./../src;

  nativeBuildInputs = [
    graphviz-nox
  ];

  buildPhase = ''
    dot -Tpdf brotherhood.dot > brotherhood.pdf
    dot -Tsvg brotherhood.dot > brotherhood.svg
    dot -Tpng brotherhood.dot > brotherhood.png
  '';

  installPhase = ''
    mkdir -p $out
    cp -r *.pdf *.svg *.png $out
  '';
}