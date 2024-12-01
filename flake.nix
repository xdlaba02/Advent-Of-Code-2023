{
	description = "Advent of Code development environment";

	inputs = {
		nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
	};

	outputs = { nixpkgs, ... }:
	let
		pkgs = import nixpkgs { system = "x86_64-linux"; };
	in {
		devShells.x86_64-linux.default = pkgs.mkShell {
			name = "aoc-dev-env";

			buildInputs = with pkgs; [
				python314
			];

			shellHook = ''
				echo "Entering Python development environment"
				if [ ! -d ".venv" ]; then
					echo "Creating venv in .venv"
					python -m venv .venv
				fi
				source .venv/bin/activate
				echo "Venv activated. Use 'deactivate' to exit."
			'';
		};
	};
}
