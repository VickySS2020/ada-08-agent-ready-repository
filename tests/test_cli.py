"""Automated CLI test suite (T-05, TS-01 through TS-11)."""
import json
import pytest
from pathlib import Path

from src.cli import format_table, main


def test_cli_search_by_name_renders_table(capsys):
    """Verify searching by name displays a structured table (TS-01, TS-04, AC-01, AC-04)."""
    exit_code = main(["--name", "Alice"])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert "| ID | Name" in captured.out
    assert "| Email" in captured.out
    assert "Alice Smith" in captured.out
    assert "alice@example.com" in captured.out


def test_cli_search_by_email_renders_table(capsys):
    """Verify searching by email displays matching customer table (TS-02, TS-04, AC-02, AC-04)."""
    exit_code = main(["--email", "bob@example.com"])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert "| ID | Name" in captured.out
    assert "Bob Jones" in captured.out
    assert "bob@example.com" in captured.out


def test_cli_search_by_email_partial(capsys):
    """Verify searching by partial email matches multiple records (TS-02, AC-02)."""
    exit_code = main(["--email", "example"])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert "Alice Smith" in captured.out
    assert "Bob Jones" in captured.out


def test_cli_unified_query_renders_table(capsys):
    """Verify unified --query searches name and email (TS-06, TS-04, AC-06, AC-04)."""
    exit_code = main(["--query", "charlie"])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert "Charlie Brown" in captured.out
    assert "charlie@domain.com" in captured.out


def test_cli_custom_file_argument(tmp_path: Path, capsys):
    """Verify CLI loads from custom file passed via --file flag (TS-07, AC-07)."""
    custom_file = tmp_path / "custom_data.json"
    custom_records = [{"id": 99, "name": "Custom Person", "email": "custom@test.com"}]
    custom_file.write_text(json.dumps(custom_records), encoding="utf-8")

    exit_code = main(["--file", str(custom_file), "--name", "Custom"])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert "Custom Person" in captured.out
    assert "custom@test.com" in captured.out


def test_cli_no_matches_message(capsys):
    """Verify informative message when no customers match (TS-05, AC-05, EH-03)."""
    exit_code = main(["--name", "NobodyHere"])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert captured.out.strip() == "MESSAGE: No customers found that matched NobodyHere"


def test_cli_empty_query_rejected(capsys):
    """Verify empty query string outputs error without crashing (TS-03, TS-09, VR-01, EH-01, AC-03)."""
    exit_code = main(["--name", ""])
    captured = capsys.readouterr()
    assert exit_code == 1
    assert captured.out.strip() == "ERROR: Invalid Input"


def test_cli_whitespace_query_rejected(capsys):
    """Verify whitespace-only query outputs error without crashing (TS-03, TS-09, VR-01, EH-01, AC-03)."""
    exit_code = main(["--query", "   "])
    captured = capsys.readouterr()
    assert exit_code == 1
    assert captured.out.strip() == "ERROR: Invalid Input"


def test_cli_omitted_search_arguments_displays_help(capsys):
    """Verify help/instructions displayed when search argument is omitted (TS-10, VR-02, EH-02)."""
    exit_code = main([])
    captured = capsys.readouterr()
    assert exit_code == 2
    assert "usage:" in captured.out or "Search customer records" in captured.out


def test_cli_storage_error_handled_gracefully(capsys):
    """Verify storage failure outputs clear error message without traceback (TS-11, VR-03, EH-04)."""
    exit_code = main(["--file", "nonexistent.json", "--name", "Alice"])
    captured = capsys.readouterr()
    assert exit_code == 1
    assert "ERROR: Failed to load customer records" in captured.out


def test_format_table_empty_list():
    """Verify format_table returns empty string for empty input."""
    assert format_table([]) == ""


def test_sort_by_name_orders_results_alphabetically(tmp_path: Path, capsys):
    """Verify --sort name returns matching records in case-insensitive alphabetical order by name (CR-01, FR-04, FR-06, AC-04)."""
    data = [
        {"id": 3, "name": "Charlie Brown", "email": "charlie@domain.com"},
        {"id": 1, "name": "Alice Smith", "email": "alice@example.com"},
        {"id": 4, "name": "alice Wonderland", "email": "alice.wonder@domain.org"},
        {"id": 2, "name": "Bob Jones", "email": "bob@example.com"},
    ]
    data_file = tmp_path / "customers.json"
    data_file.write_text(json.dumps(data), encoding="utf-8")

    exit_code = main(["--file", str(data_file), "--query", "a", "--sort", "name"])
    captured = capsys.readouterr()
    assert exit_code == 0

    # All four records match "a" (present in every name)
    lines = [l for l in captured.out.splitlines() if "|" in l and "Name" not in l]
    names_in_output = [l.split("|")[2].strip() for l in lines]
    assert names_in_output == sorted(names_in_output, key=str.lower)
    # Verify table columns are present
    assert "| ID" in captured.out
    assert "| Name" in captured.out
    assert "| Email" in captured.out


def test_sort_by_email_orders_results_alphabetically(tmp_path: Path, capsys):
    """Verify --sort email returns matching records in case-insensitive alphabetical order by email (CR-01, FR-04, FR-06, AC-04)."""
    data = [
        {"id": 3, "name": "Charlie Brown", "email": "charlie@domain.com"},
        {"id": 1, "name": "Alice Smith", "email": "alice@example.com"},
        {"id": 4, "name": "Alice Wonderland", "email": "Alice.wonder@domain.org"},
        {"id": 2, "name": "Bob Jones", "email": "bob@example.com"},
    ]
    data_file = tmp_path / "customers.json"
    data_file.write_text(json.dumps(data), encoding="utf-8")

    exit_code = main(["--file", str(data_file), "--query", "a", "--sort", "email"])
    captured = capsys.readouterr()
    assert exit_code == 0

    lines = [l for l in captured.out.splitlines() if "|" in l and "Email" not in l]
    emails_in_output = [l.split("|")[3].strip() for l in lines]
    assert emails_in_output == sorted(emails_in_output, key=str.lower)
    assert "| ID" in captured.out
    assert "| Email" in captured.out


def test_sort_does_not_change_matched_records(tmp_path: Path, capsys):
    """Verify --sort does not filter or add records — same set returned as without sort (CR-01)."""
    data = [
        {"id": 1, "name": "Alice Smith", "email": "alice@example.com"},
        {"id": 2, "name": "Bob Jones", "email": "bob@example.com"},
        {"id": 3, "name": "Charlie Brown", "email": "charlie@domain.com"},
    ]
    data_file = tmp_path / "customers.json"
    data_file.write_text(json.dumps(data), encoding="utf-8")

    exit_code_sorted = main(["--file", str(data_file), "--name", "alice", "--sort", "name"])
    captured_sorted = capsys.readouterr()

    exit_code_unsorted = main(["--file", str(data_file), "--name", "alice"])
    captured_unsorted = capsys.readouterr()

    assert exit_code_sorted == 0
    assert exit_code_unsorted == 0
    # Both outputs contain the same customer name
    assert "Alice Smith" in captured_sorted.out
    assert "Alice Smith" in captured_unsorted.out
    # Neither output contains non-matching customers
    assert "Bob Jones" not in captured_sorted.out
    assert "Charlie Brown" not in captured_sorted.out


def test_sort_without_sort_flag_unchanged(tmp_path: Path, capsys):
    """Verify that omitting --sort preserves existing behaviour (CR-01)."""
    data = [
        {"id": 2, "name": "Bob Jones", "email": "bob@example.com"},
        {"id": 1, "name": "Alice Smith", "email": "alice@example.com"},
    ]
    data_file = tmp_path / "customers.json"
    data_file.write_text(json.dumps(data), encoding="utf-8")

    exit_code = main(["--file", str(data_file), "--query", "example"])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert "Alice Smith" in captured.out
    assert "Bob Jones" in captured.out


def test_sort_invalid_choice_rejected(capsys):
    """Verify --sort rejects values other than 'name' and 'email'."""
    with pytest.raises(SystemExit) as exc_info:
        main(["--name", "Alice", "--sort", "id"])
    assert exc_info.value.code != 0


def test_format_table_output_structure():
    """Verify table format creates aligned rows and header separator (TS-04, AC-04)."""
    sample = [
        {"id": 1, "name": "Alice Smith", "email": "alice@example.com"},
        {"id": 200, "name": "Bob", "email": "bob@example.com"},
    ]
    table = format_table(sample)
    lines = table.splitlines()
    assert len(lines) >= 5
    assert "+-" in lines[0]
    assert "| ID " in lines[1]
    assert "| Name " in lines[1]
    assert "| Email " in lines[1]
    assert "Alice Smith" in table
    assert "200" in table
