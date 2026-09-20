import typer
from simulation import run_simulation

def main(filename: str, generations: int = typer.Argument(10)) -> None:
    run_simulation(filename,generations)
    
if __name__ =="__main__":
    typer.run(main)