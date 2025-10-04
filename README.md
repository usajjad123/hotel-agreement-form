# Hotel Agreement Form Generator

A modern, user-friendly web application for generating hotel agreement PDFs. This application replaces the old CLI-based workflow with a beautiful, responsive web interface.

## Features

- 🎨 **Modern UI/UX**: Beautiful, responsive design with smooth animations
- 📱 **Mobile Friendly**: Works perfectly on desktop, tablet, and mobile devices
- ✅ **Form Validation**: Real-time validation with helpful error messages
- 👀 **Preview Mode**: Preview your form data before generating PDF
- 🔄 **Auto-calculations**: Automatically calculates remaining balance
- ⌨️ **Keyboard Shortcuts**: Ctrl/Cmd + Enter to submit, Escape to close modals
- 📄 **PDF Generation**: Generates professional PDF agreements using your existing template

## Prerequisites

- Python 3.7 or higher
- The original `SAMPLE AGREEMENT.jpg` file
- The `Futura Book font.ttf` font file

## Installation

1. **Clone or download this project**

2. **Set up the virtual environment and install dependencies**:
   ```bash
   python setup.py
   ```
   This will:
   - Create a virtual environment
   - Install all required dependencies
   - Set up the project structure
   - Create activation scripts

3. **Ensure required files are present**:
   - `SAMPLE AGREEMENT.jpg` (your agreement template)
   - `Futura Book font.ttf` (your custom font)

## Usage

### Starting the Application

**Option 1: Using the provided scripts (Recommended)**

- **Windows**: Double-click `start.bat`
- **macOS/Linux**: Run `./start.sh`

**Option 2: Manual activation**

1. **Activate the virtual environment**:
   - **Windows**: Run `venv\Scripts\activate`
   - **macOS/Linux**: Run `source venv/bin/activate`

2. **Start the Flask server**:
   ```bash
   python app.py
   ```

3. **Open your browser** and go to:
   ```
   http://localhost:5000
   ```

### Using the Form

1. **Fill in the form fields**:
   - **Personal Information**: Name, nationality, phone, residence type, passport/ID
   - **Agreement Details**: Check-in/out dates, rent description, amounts, room details

2. **Preview your data** (optional):
   - Click the "Preview" button to review all entered information

3. **Generate PDF**:
   - Click "Generate PDF" to create and download your agreement

### Form Fields Explained

| Field | Description | Example |
|-------|-------------|---------|
| Full Name | Guest's complete name | ABDULLAH MOHAMMAD SAYEM |
| Nationality | Guest's nationality | BANGLADESH |
| Phone Number | Contact number | 0556825302 |
| Residence Type | Type of residence | RESIDENCE |
| Passport/ID Number | Identification number | 2564390371 |
| Check-in Date | Arrival date | 25/07/2025 |
| Check-out Date | Departure date | 31/08/2025 |
| Rent Description | Detailed rent breakdown | MONTHLY RENT 1500/-JULY 6 DAYS 300/- |
| Total Amount | Total rent amount | 1800 |
| Advance Payment | Initial payment made | 500 |
| Balance Details | Payment schedule | 1300 BAL AMT WILL PAY 2/7/25 |
| Remaining Balance | Outstanding amount | 0 |
| Room Details | Room information | H1-601. 2ROOM |

## File Structure

```
hotel-agreement-form/
├── setup.py              # Virtual environment setup script
├── app.py                # Flask server
├── config.py             # Configuration settings
├── requirements.txt      # Python dependencies
├── README.md            # This file
├── LICENSE              # License file
├── SAMPLE_AGREEMENT.jpg # Your agreement template
├── Futura Book font.ttf # Custom font
├── start.py             # Startup script
├── start.bat            # Windows startup script
├── start.sh             # macOS/Linux startup script
├── venv/                # Virtual environment (created by setup.py)
│   ├── bin/             # Virtual environment binaries
│   ├── lib/             # Installed packages
│   └── pyvenv.cfg       # Virtual environment config
├── static/             # Web assets
│   ├── index.html       # Main form page
│   ├── styles.css       # Styling
│   └── script.js        # JavaScript functionality
```

## Development

### Customizing the Form

- **Styling**: Edit `static/styles.css` to change colors, fonts, and layout
- **Functionality**: Modify `static/script.js` for additional features
- **Backend**: Update `app.py` for server-side changes

### Adding New Fields

1. Add the field to the HTML form in `static/index.html`
2. Update the field mapping in `static/script.js`
3. Add the field to the backend processing in `app.py`

## Troubleshooting

### Common Issues

1. **"Sample agreement image not found"**
   - Ensure `SAMPLE AGREEMENT.jpg` is in the project root

2. **"Font file not found"**
   - Ensure `Futura Book font.ttf` is in the project root

3. **Port already in use**
   - Change the port in `app.py` or kill the existing process

4. **PDF generation fails**
   - Check that all required files are present
   - Verify Python dependencies are installed

### Getting Help

- Check the browser console for JavaScript errors
- Check the terminal for Python/Flask errors
- Ensure all required files are in the correct locations

## Migration from Old System

### Old Workflow
1. Edit `form.txt` with values
2. Run `program.bat`
3. Find PDF in `ALL_AGREEMENTS/` folder

### New Workflow
1. Open web browser
2. Fill out form
3. Click "Generate PDF"
4. PDF downloads automatically

## Browser Compatibility

- ✅ Chrome (recommended)
- ✅ Firefox
- ✅ Safari
- ✅ Edge
- ❌ Internet Explorer (not supported)

## License

This project is for internal use. Please ensure compliance with your organization's policies.

---

**Note**: This application maintains the same PDF generation logic as your original script while providing a much better user experience through a modern web interface. 