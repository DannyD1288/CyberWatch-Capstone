# Test Plan and Results

## Test approach
Test detection boundaries, input validation, UI search/filter behavior, alert resolution, and local setup.

## Evidence available
The supplied `test_results.txt` records **5 passing pytest detection tests** (October 10, 2026). An independent check of the detection function was also completed during packaging: all five logic scenarios passed, and the supplied sample CSV generated one alert from seven events. These independent checks do not replace a full Flask integration test.

## Test cases
| Case | Expected | Evidence/status |
|---|---|---|
| Five failures within five minutes, same IP | Alert | Passed (prior pytest and independent logic check) |
| Four failures | No alert | Passed (prior pytest and independent logic check) |
| Successful logins | No alert | Passed (prior pytest and independent logic check) |
| Five failures across different IPs | No alert | Passed (prior pytest and independent logic check) |
| Five failures outside window | No alert | Passed (prior pytest and independent logic check) |
| Sample CSV: six failures and one success | Seven events, one alert | Passed (independent logic check) |
| Invalid CSV input cases | Helpful validation errors | Input files included; full browser verification pending |
| Search, status filters, and alert resolution | Correct interactive behavior | Manual end-to-end retest recommended |

## Run automated tests
`python -m pytest tests/ -v`

## Submission check
Run the application, upload the sample CSV to a fresh database, verify one alert, test filters and Resolve, and capture current screenshots. Do not claim unperformed browser checks passed.
