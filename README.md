# 🛡️ Password Strength Evaluation & Security Best Practices

## Objective:

The goal of this task is to explore the effectiveness of different password strengths, learn password creation best practices, understand how common attacks exploit weak passwords, and summarize how password complexity impacts security.

## 📝 Steps Performed 

1. Created multiple passwords with varying complexity.
   Used uppercase, lowercase, numbers, symbols, and length variations.

| Password Sample | Type |
| --- | --- |
| password123 | 🔴 Very Weak |
| WhoAmI23 | 🟠 Weak |
| Why#Pass01 | 🟡 Medium |
| Why@Typepass&1 | 🟢 Strong |
| Boogie&Woggie#01 | 🟢 Very Strong |


2. Test each password on password strength checker.

   [Bitwarden Strength Tester](https://bitwarden.com/password-strength/)
   
   [Password Monster](https://www.passwordmonster.com/)
   
   [How Secure Is My Password](https://www.security.org/how-secure-is-my-password/)
   
   
4. Results & Feedback

| Password Sample | Estimated Crack Time | Tool Feedback|
| --- | --- | --- |
| password123 | Few seconds or <1 second | Very Weak |
| WhoAmI23 | Few Minutes | Weak |
| Why#Pass01 | Few Hours to Week | Medium |
| Why@Typepass&0 | Months to Years | Strong |
| Boogie&Woggie#01 | 1 million years | Very Strong |

- Password Strength Results from Bitwarden & Password Monster:
  
  [Results](https://github.com/hellolightning/Elevate-Labs/blob/Task-6/Results.md)

## 



## 🔐 Best Practices for Strong and Secured Passwords

### Length and Complexity:
- Minimum Length: Use for at least 12-16 or more characters, longer passwords are inherently more secure.
- Character Variety: Include a mix of uppercase letters, lowercase letters, numbers, and special characters (e.g., !, @, #, $, %). 

### Avoid Predictable Elements:
- No Personal Information: Do not use easily discoverable details like your name, birthdate, pet's name, or address.
- No Dictionary Words or Common Phrases: Avoid using words found in dictionaries or simple, common phrases.
- No Sequential or Repetitive Patterns: Steer clear of patterns like "123456,"qwerty," or "aaaaaa."

### Uniqueness:
- Never reuse passwords across different accounts. A breach of one account could compromise all others using the same password.

### Avoid Browser Autofill:
- Not recommended for sensitive accounts; password managers are safer.

### Update Regularly: 
- Change passwords for sensitive accounts every few months.

### Password Managers:
- Utilize a reputable password manager to securely generate, store, and manage unique and complex passwords for all your accounts. 
- This eliminates the need to remember numerous complex strings and enhances overall security.

## 🔐 Password Security Tips & Insights

- Avoid using the same password everywhere.
- Never use personal info (name, birthday, etc.)
- Include uppercase, lowercase, numbers, and symbols
- Avoid using dictionary words or predictable sequences
- Use a password manager it encrypts your passwords and credentials and help you organize them securely.
- MFA/2FA is essential for all important accounts.

## 🚨 Common Password Attacks & Defenses

| Attack Type	| Description |	Defense |
| --- | --- | --- |
| Brute Force |	Tries all possible combinations	| Long, complex passwords |
| Dictionary Attack |	Uses common words/phrases |	Avoid dictionary words & common substitutions |
| Credential Stuffing |	Uses leaked password pairs | Unique passwords for every account |
| Keylogger	| Captures keystrokes |	Use security software, avoid suspicious links |
| Rainbow Table |	Precomputed hash tables	| Use strong, salted hashes (for admins) |

## Conclusion

This task demonstrated how password complexity greatly affects security, showing that longer, more varied passwords are far harder to crack. Following best practices and using unique, complex passwords with a password manager significantly improves protection against attacks.


