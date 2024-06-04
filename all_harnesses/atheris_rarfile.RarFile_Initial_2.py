
import atheris
import sys
import io
import rarfile

# Ensure all necessary imports for fuzzing are instrumented for coverage.
with atheris.instrument_imports():
    # Import other dependencies needed for fuzz testing here.
    pass

def TestOneInput(data):
    try:
        # Attempt to open the rar file from in-memory bytes. This uses the fuzzed data.
        with rarfile.RarFile(io.BytesIO(data)) as rf:
            # Iterate over rf.infolist() to force parsing of the contained files' metadata, enhancing fuzzing coverage.
            # Accessing rf.read() on file entries could increase code paths exercised during fuzzing but may require valid archives.
            for f in rf.infolist():
                try:
                    _ = rf.read(f)  # Consider this extension to increase interaction with the rarfile module.
                except rarfile.Error:
                    # An expected error when attempting to read a file from a potentially malformed archive.
                    pass
    except rarfile.Error:
        # This exception is expected for invalid or unsupported RAR archives.
        pass
    except Exception as e:
        # Log or process unexpected exceptions without stopping the fuzzer.
        # This ensures broader exception coverage and helps identify unforeseen bugs.
        print(f"Caught unexpected exception: {e}")

# Set up Atheris with the entry point (TestOneInput) and the necessary arguments (sys.argv).
atheris.Setup(sys.argv, TestOneInput)

if __name__ == "__main__":
    # Execute the fuzzer.
    atheris.Fuzz()
