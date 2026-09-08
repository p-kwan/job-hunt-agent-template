from job_search_agent.main import main


def test_main_runs(capsys):
    main()
    captured = capsys.readouterr()
    assert "job-search-agent" in captured.out
