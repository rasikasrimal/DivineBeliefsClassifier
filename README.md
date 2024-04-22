# DivineBeliefsClassifier 🛐

DivineBeliefsClassifier is an interactive Python program designed to help users explore and discover religions based on their beliefs. Through a series of questions, users can navigate various belief systems and find the one that resonates with them.

## How to Use

1. Clone the repository to your local machine.
2. Ensure you have Python installed.
3. Navigate to the directory containing the program.
4. Run the program by executing `python religion_selector.py`.
5. Follow the prompts to answer the questions.
6. Based on your responses, the program will suggest a religion that best suits your beliefs.

````markdown
How many gods do you believe in?
├── None
│   ├── Do you believe in any kind of spirituality?
│       ├── No : Atheist
│       └── Yes
│           ├── Should you deny yourself pleasures?
│               ├── Yes : Buddhism
│               └── No : Spiritual but not religious
├── One
│   ├── Is God separate from the universe?
│       ├── Yes
│           ├── Does God interact with the universe?
│           │   ├── No : Deist
│           │   └── Yes
│           │       ├── Did God become human in Jesus?
│           │           ├── Yes : Christian
│           │           └── No
│           │               ├── Is Jesus still the messiah?
│           │                   ├── No : Jewish
│           │                   └── Yes : Muslim
│           └── No
│               ├── Can you worship idols?
│                   ├── Yes : Hindu
│                   └── No : Sikh
└── Many
    ├── Do you believe in reincarnation?
        ├── No : Pagan
        └── Yes : Hindu
