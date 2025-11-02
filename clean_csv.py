import glob
import os

def clean_csv_file(filepath):
    """Remove trailing empty lines from CSV files"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Remove trailing empty lines
        while lines and lines[-1].strip() == '':
            lines.pop()
        
        # Write back (with final newline)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(lines)
            if lines and not lines[-1].endswith('\n'):
                f.write('\n')
        
        print(f"✓ Cleaned: {filepath}")
        return True
    except Exception as e:
        print(f"✗ Error cleaning {filepath}: {e}")
        return False

# Process all CSV files
csv_files = glob.glob('data/*.csv') + glob.glob('config/*.csv')
print(f"Found {len(csv_files)} CSV files to clean\n")

success_count = 0
for csv_file in csv_files:
    if clean_csv_file(csv_file):
        success_count += 1

print(f"\n✅ Successfully cleaned {success_count}/{len(csv_files)} files")

