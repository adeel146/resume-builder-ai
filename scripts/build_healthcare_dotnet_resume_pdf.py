"""Build the healthcare .NET resume using the shared Markdown PDF renderer."""

from build_deel_resume_pdf import ROOT, build


if __name__ == "__main__":
    build(
        source_path=ROOT / "jobs" / "healthcare-dotnet" / "targeted-resume.md",
        output_path=(
            ROOT / "output" / "healthcare-dotnet"
            / "Muhammad_Adeel_Senior_DotNet_Software_Engineer.pdf"
        ),
        title="Muhammad Adeel - Senior .NET Software Engineer",
    )
