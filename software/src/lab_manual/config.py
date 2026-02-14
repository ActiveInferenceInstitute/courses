"""Configuration constants for lab manual rendering."""

from typing import Any, Dict, List

# Lab manual-specific CSS for print-friendly, fillable worksheets
LAB_MANUAL_CSS = """
/* Lab Manual Worksheet Styles - Black/White/Gray with Red Accents */
@page {
    size: letter;
    margin: 0.75in;
}

body {
    font-family: 'Georgia', 'Times New Roman', serif;
    font-size: 11pt;
    line-height: 1.5;
    color: #1a1a1a;
    background-color: #ffffff;
}

h1 {
    font-size: 18pt;
    font-weight: bold;
    text-align: center;
    margin-bottom: 0.5em;
    border-bottom: 3px solid #c41e3a;
    padding-bottom: 0.3em;
    color: #1a1a1a;
}

h2 {
    font-size: 14pt;
    font-weight: bold;
    margin-top: 1.5em;
    margin-bottom: 0.5em;
    color: #c41e3a;
    border-left: 4px solid #c41e3a;
    padding-left: 0.5em;
}

h3 {
    font-size: 12pt;
    font-weight: bold;
    margin-top: 1em;
    margin-bottom: 0.3em;
    color: #333333;
}

/* Horizontal rules */
hr {
    border: none;
    border-top: 1px solid #cccccc;
    margin: 1.5em 0;
}

/* Lab Header Info */
.lab-header {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1em;
    margin-bottom: 1.5em;
    padding: 1em;
    border: 1px solid #333333;
    background-color: #f5f5f5;
}

.lab-header-field {
    display: flex;
    align-items: baseline;
    gap: 0.5em;
}

.lab-header-label {
    font-weight: bold;
    white-space: nowrap;
    color: #1a1a1a;
}

.lab-header-value {
    flex: 1;
    border-bottom: 1px solid #333333;
    min-height: 1.5em;
}

/* Data Tables */
.lab-table {
    width: 100%;
    border-collapse: collapse;
    margin: 1em 0;
}

.lab-table th {
    background-color: #333333;
    color: #ffffff;
    font-weight: bold;
    text-align: left;
    padding: 8px 12px;
    border: 1px solid #1a1a1a;
}

.lab-table td {
    padding: 8px 12px;
    border: 1px solid #333333;
    min-height: 2em;
    vertical-align: top;
}

.lab-table td.fillable {
    background-color: #fafafa;
    min-height: 2.5em;
}

.lab-table tr:nth-child(even) {
    background-color: #f0f0f0;
}

/* Fillable Fields */
.fill-text {
    display: inline-block;
    min-width: 200px;
    border-bottom: 1px solid #333333;
    padding: 2px 4px;
    background-color: #fafafa;
}

.fill-number {
    display: inline-block;
    min-width: 60px;
    max-width: 100px;
    border-bottom: 1px solid #333333;
    padding: 2px 4px;
    background-color: #fafafa;
    text-align: center;
}

/* Inline tables inside reflection/calculation boxes */
.reflection-box table,
.calculation-box table {
    width: 100%;
    border-collapse: collapse;
    margin: 0.5em 0;
}

.reflection-box th,
.calculation-box th {
    background-color: #333333;
    color: #ffffff;
    font-weight: bold;
    text-align: left;
    padding: 6px 10px;
    border: 1px solid #1a1a1a;
}

.reflection-box td,
.calculation-box td {
    padding: 6px 10px;
    border: 1px solid #333333;
    vertical-align: top;
}

.reflection-box tr:nth-child(even),
.calculation-box tr:nth-child(even) {
    background-color: #f0f0f0;
}

.fill-textarea {
    display: block;
    width: 100%;
    min-height: 3em;
    border: 1px solid #333333;
    padding: 8px;
    margin: 0.5em 0;
    background-color: #fafafa;
}

/* Drawing Areas - Blank Space for Student Drawings */
.fill-drawing {
    display: block;
    width: 100%;
    border: 2px solid #333333;
    margin: 1em 0;
    background-color: #ffffff;
    box-sizing: border-box;
}

.fill-drawing-circle {
    display: block;
    border: 2px solid #333333;
    border-radius: 50%;
    margin: 1em auto;
    background-color: #ffffff;
    box-sizing: border-box;
}

.fill-checkbox {
    display: flex;
    align-items: flex-start;
    gap: 0.5em;
    margin: 0.3em 0;
}

.fill-checkbox input[type="checkbox"] {
    width: 1em;
    height: 1em;
    margin-top: 0.25em;
    accent-color: #c41e3a;
}

/* Measurement Table */
.measurement-table {
    width: 100%;
    border-collapse: collapse;
    margin: 1em 0;
}

.measurement-table th {
    background-color: #1a1a1a;
    color: #ffffff;
    font-weight: bold;
    text-align: center;
    padding: 10px 12px;
    border: 1px solid #000000;
}

.measurement-table td {
    padding: 12px;
    border: 1px solid #333333;
    text-align: center;
}

.measurement-table td.fillable {
    background-color: #fafafa;
    min-height: 3em;
}

.measurement-table .row-number {
    width: 40px;
    background-color: #e0e0e0;
    font-weight: bold;
    color: #333333;
}

/* Object Selection Section */
.object-selection {
    margin: 1em 0;
    padding: 1em;
    border: 2px solid #1a1a1a;
    border-radius: 4px;
    background-color: #f5f5f5;
    border-left: 5px solid #c41e3a;
}

.object-selection h3 {
    margin-top: 0;
    color: #1a1a1a;
}

.object-field {
    display: flex;
    align-items: baseline;
    gap: 0.5em;
    margin: 1em 0;
}

.object-label {
    font-weight: bold;
    min-width: 150px;
    color: #333333;
}

.object-input {
    flex: 1;
    border-bottom: 2px solid #333333;
    min-height: 1.5em;
    background-color: #ffffff;
    padding: 4px;
}

/* Feasibility Section */
.feasibility-section {
    margin: 1em 0;
    padding: 1em;
    border: 1px solid #999999;
    border-radius: 4px;
    background-color: #fafafa;
}

.feasibility-question {
    font-weight: bold;
    margin-bottom: 0.5em;
    color: #1a1a1a;
}

.feasibility-options {
    margin-left: 1em;
}

/* Calculation Box */
.calculation-box {
    margin: 1em 0;
    padding: 1em;
    border: 2px solid #999999;
    border-left: 4px solid #2563eb;
    background-color: #f8fafc;
    min-height: 60px;
}

.calculation-box code {
    font-family: 'Courier New', Courier, monospace;
    background-color: #e8e8e8;
    padding: 1px 4px;
    border-radius: 2px;
}

.calculation-box pre {
    background-color: #f0f0f0;
    padding: 0.75em;
    border-radius: 4px;
    border: 1px solid #cccccc;
    font-family: 'Courier New', Courier, monospace;
    font-size: 10pt;
    overflow-x: auto;
}

/* Reflection Box */
.reflection-box {
    margin: 1em 0;
    padding: 1em;
    border: 2px solid #666666;
    border-left: 4px solid #c41e3a;
    background-color: #fafafa;
    min-height: 100px;
}

/* Blockquotes (Learning Goals) */
blockquote {
    margin: 1em 0;
    padding: 0.75em 1em;
    border-left: 4px solid #c41e3a;
    background-color: #f9f9f9;
    font-style: italic;
    color: #333333;
}

blockquote strong {
    color: #c41e3a;
}

/* Strong emphasis */
strong {
    color: #1a1a1a;
}

/* Emphasis within reflection */
em {
    color: #555555;
}

/* Lists */
ul, ol {
    margin-left: 1.5em;
}

li {
    margin: 0.3em 0;
}

/* Summary table */
.summary-table th {
    background-color: #c41e3a;
    color: #ffffff;
}

/* Print Styles */
@media print {
    .lab-table td.fillable,
    .fill-text,
    .fill-textarea,
    .object-input {
        background-color: white !important;
    }
    
    .no-print {
        display: none !important;
    }
    
    h1, h2, h3 {
        page-break-after: avoid;
    }
    
    .lab-table, .measurement-table {
        page-break-inside: avoid;
    }
    
    blockquote {
        background-color: white !important;
    }
}
"""

# HTML template for lab manual
LAB_HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
{css}
    </style>
</head>
<body>
    <div class="lab-manual">
        {content}
    </div>
    <script>
{javascript}
    </script>
</body>
</html>
"""

# Default PDF generation options
DEFAULT_PDF_OPTIONS: Dict[str, Any] = {
    "page_size": "letter",
    "margin_top": "0.75in",
    "margin_bottom": "0.75in",
    "margin_left": "0.75in",
    "margin_right": "0.75in",
}

# Lab element directive patterns
LAB_DIRECTIVES = {
    "data-table": r"<!-- lab:data-table(.*)-->(.*)<!-- /lab:data-table -->",
    "object-selection": r"<!-- lab:object-selection -->(.*)<!-- /lab:object-selection -->",
    "measurement-feasibility": r"<!-- lab:measurement-feasibility -->(.*)<!-- /lab:measurement-feasibility -->",
    "reflection": r"<!-- lab:reflection -->(.*)<!-- /lab:reflection -->",
    "calculation": r"<!-- lab:calculation -->(.*)<!-- /lab:calculation -->",
}

# Default measurement table columns
DEFAULT_MEASUREMENT_COLUMNS: List[str] = [
    "Physical Aspect",
    "Measurement Device",
    "Measurement Unit",
]

# Default number of rows for data tables
DEFAULT_TABLE_ROWS = 5

# Interactive JavaScript for HTML output
LAB_INTERACTIVE_JS = """
// Lab Manual Interactive Functions

// Auto-save form data to localStorage
function saveLabData() {
    const form = document.querySelector('.lab-manual');
    const inputs = form.querySelectorAll('input, textarea');
    const data = {};
    inputs.forEach((input, idx) => {
        const key = input.id || input.name || `field_${idx}`;
        if (input.type === 'checkbox') {
            data[key] = input.checked;
        } else {
            data[key] = input.value;
        }
    });
    localStorage.setItem('labManualData_' + document.title, JSON.stringify(data));
    showSaveNotification();
}

// Load saved form data
function loadLabData() {
    const saved = localStorage.getItem('labManualData_' + document.title);
    if (saved) {
        const data = JSON.parse(saved);
        const form = document.querySelector('.lab-manual');
        const inputs = form.querySelectorAll('input, textarea');
        inputs.forEach((input, idx) => {
            const key = input.id || input.name || `field_${idx}`;
            if (data[key] !== undefined) {
                if (input.type === 'checkbox') {
                    input.checked = data[key];
                } else {
                    input.value = data[key];
                }
            }
        });
    }
}

// Show save notification
function showSaveNotification() {
    let notification = document.getElementById('save-notification');
    if (!notification) {
        notification = document.createElement('div');
        notification.id = 'save-notification';
        notification.style.cssText = 'position: fixed; bottom: 20px; right: 20px; background: #c41e3a; color: white; padding: 10px 20px; border-radius: 4px; opacity: 0; transition: opacity 0.3s;';
        document.body.appendChild(notification);
    }
    notification.textContent = 'Progress saved!';
    notification.style.opacity = '1';
    setTimeout(() => { notification.style.opacity = '0'; }, 2000);
}

// Clear all data
function clearLabData() {
    if (confirm('Clear all entered data? This cannot be undone.')) {
        localStorage.removeItem('labManualData_' + document.title);
        location.reload();
    }
}

// Print lab manual
function printLabManual() {
    window.print();
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    loadLabData();
    
    // Auto-save on input
    const form = document.querySelector('.lab-manual');
    if (form) {
        form.addEventListener('input', () => {
            clearTimeout(window.saveTimeout);
            window.saveTimeout = setTimeout(saveLabData, 1000);
        });
    }
});
"""
