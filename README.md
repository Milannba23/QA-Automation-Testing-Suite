# 🚀 QA Automation Suite: KupujemProdajem (Python & Selenium)

Professional automated UI testing suite for Serbia's leading e-commerce platform. This project demonstrates high-level automation patterns, including **Robust Locators**, **Synchronization Strategies**, and **Fallback Logic**.


## 🛠️ Tech Stack & Tools
- **Language:** Python 3.10+
- **Core Engine:** Selenium WebDriver
- **Test Framework:** PyTest
- **Drivers:** WebDriver Manager (Chrome)
- **Visual Evidence:** YouTube Demo & Local Screenshots

## 🌟 QA Engineering Highlights
- **Smart Locators**: Implementation of `@data-testid` attributes and complex XPaths to ensure test stability against UI changes.
- **Robust Error Handling**: Advanced "Fallback" strategy that automatically switches to alternative selectors if primary ones fail.
- **Dynamic Synchronization**: Heavy use of `WebDriverWait` and `Expected Conditions` to eliminate "flaky" tests caused by async loading.
- **User Behavior Emulation**: Includes automatic scrolling (`window.scrollBy`) to ensure elements are interactable before execution.


## 🎥 Test Execution & Visual Evidence

Witness the automation in action. These videos and screenshots confirm the reliability of the testing suite.

### ✅ Scenario 1: Advanced Price Filtering (iPhone 15)
*Verifies that the system accurately filters products within a specific price range (500€ - 1000€).*
- **Watch Video:** [▶️ Click here to watch on YouTube](https://youtu.be/Y28iyIS8Ilk)
- **Evidence:** ![Price Range Validation](./media/price-range-validation.png)

### ✅ Scenario 2: Search Engine Stability
*Validates the core search functionality and ensures the UI renders correctly after queries.*
- **Watch Video:** [▶️ Click here to watch on YouTube](https://youtu.be/P_xRzxUJJO4)
- **Evidence:** ![Search Success Confirmation](./media/search-results-confirmation.png)


## 📂 Project Structure & Key Files

- `test_search_filters_advanced.py`: Test script utilizing high-stability `@data-testid` selectors.
- `test_price_filter_robust.py`: Test script implementing Fallback logic and scrolling techniques.
- `/media`: Contains visual proof and screenshots of successful test runs.

## 🚀 Getting Started
1. **Clone the repository:**
   
   git clone [https://github.com/Milannba23/QA-Automation-Testing-Suite.git](https://github.com/Milannba23/QA-Automation-Testing-Suite.git)