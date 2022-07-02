# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'options_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OptionsDialog(object):
    def setupUi(self, OptionsDialog):
        OptionsDialog.setObjectName("OptionsDialog")
        OptionsDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        OptionsDialog.resize(531, 330)
        OptionsDialog.setModal(True)
        self.options_vert_layout = QtWidgets.QVBoxLayout(OptionsDialog)
        self.options_vert_layout.setObjectName("options_vert_layout")
        self.tabs_widget = QtWidgets.QTabWidget(OptionsDialog)
        self.tabs_widget.setObjectName("tabs_widget")
        self.appearance_tab = QtWidgets.QWidget()
        self.appearance_tab.setEnabled(True)
        self.appearance_tab.setObjectName("appearance_tab")
        self.appearance_tab_layout = QtWidgets.QVBoxLayout(self.appearance_tab)
        self.appearance_tab_layout.setObjectName("appearance_tab_layout")
        self.appearance_vert_layout = QtWidgets.QVBoxLayout()
        self.appearance_vert_layout.setContentsMargins(12, 12, 12, 12)
        self.appearance_vert_layout.setObjectName("appearance_vert_layout")
        self.appearance_grid_layout = QtWidgets.QGridLayout()
        self.appearance_grid_layout.setObjectName("appearance_grid_layout")
        self.use_calendar_checkbox = QtWidgets.QCheckBox(self.appearance_tab)
        self.use_calendar_checkbox.setChecked(True)
        self.use_calendar_checkbox.setObjectName("use_calendar_checkbox")
        self.appearance_grid_layout.addWidget(self.use_calendar_checkbox, 1, 2, 1, 1)
        self.min_line = QtWidgets.QLineEdit(self.appearance_tab)
        self.min_line.setObjectName("min_line")
        self.appearance_grid_layout.addWidget(self.min_line, 11, 1, 1, 2)
        self.primary_color_button = QtWidgets.QPushButton(self.appearance_tab)
        self.primary_color_button.setObjectName("primary_color_button")
        self.appearance_grid_layout.addWidget(self.primary_color_button, 12, 1, 1, 1)
        self.secondary_color_preview = QtWidgets.QLabel(self.appearance_tab)
        self.secondary_color_preview.setStyleSheet("background-color: #ADC;")
        self.secondary_color_preview.setObjectName("secondary_color_preview")
        self.appearance_grid_layout.addWidget(self.secondary_color_preview, 13, 2, 1, 1)
        self.hrs_label = QtWidgets.QLabel(self.appearance_tab)
        self.hrs_label.setObjectName("hrs_label")
        self.appearance_grid_layout.addWidget(self.hrs_label, 10, 0, 1, 1)
        self.week_start_label = QtWidgets.QLabel(self.appearance_tab)
        self.week_start_label.setObjectName("week_start_label")
        self.appearance_grid_layout.addWidget(self.week_start_label, 3, 0, 1, 1)
        self.hrs_line = QtWidgets.QLineEdit(self.appearance_tab)
        self.hrs_line.setObjectName("hrs_line")
        self.appearance_grid_layout.addWidget(self.hrs_line, 10, 1, 1, 2)
        self.primary_color_preview = QtWidgets.QLabel(self.appearance_tab)
        self.primary_color_preview.setStyleSheet("background-color: #BDC;")
        self.primary_color_preview.setObjectName("primary_color_preview")
        self.appearance_grid_layout.addWidget(self.primary_color_preview, 12, 2, 1, 1)
        self.secondary_color_label = QtWidgets.QLabel(self.appearance_tab)
        self.secondary_color_label.setObjectName("secondary_color_label")
        self.appearance_grid_layout.addWidget(self.secondary_color_label, 13, 0, 1, 1)
        self.total_line = QtWidgets.QLineEdit(self.appearance_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.total_line.sizePolicy().hasHeightForWidth())
        self.total_line.setSizePolicy(sizePolicy)
        self.total_line.setObjectName("total_line")
        self.appearance_grid_layout.addWidget(self.total_line, 7, 1, 1, 2)
        self.range_select_dropdown = QtWidgets.QComboBox(self.appearance_tab)
        self.range_select_dropdown.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.range_select_dropdown.setObjectName("range_select_dropdown")
        self.range_select_dropdown.addItem("")
        self.range_select_dropdown.addItem("")
        self.range_select_dropdown.addItem("")
        self.range_select_dropdown.addItem("")
        self.range_select_dropdown.addItem("")
        self.appearance_grid_layout.addWidget(self.range_select_dropdown, 1, 1, 1, 1)
        self.week_start_dropdown = QtWidgets.QComboBox(self.appearance_tab)
        self.week_start_dropdown.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.week_start_dropdown.setObjectName("week_start_dropdown")
        self.week_start_dropdown.addItem("")
        self.week_start_dropdown.addItem("")
        self.week_start_dropdown.addItem("")
        self.week_start_dropdown.addItem("")
        self.week_start_dropdown.addItem("")
        self.week_start_dropdown.addItem("")
        self.week_start_dropdown.addItem("")
        self.appearance_grid_layout.addWidget(self.week_start_dropdown, 3, 1, 1, 1)
        self.min_label = QtWidgets.QLabel(self.appearance_tab)
        self.min_label.setObjectName("min_label")
        self.appearance_grid_layout.addWidget(self.min_label, 11, 0, 1, 1)
        self.range_select_label = QtWidgets.QLabel(self.appearance_tab)
        self.range_select_label.setObjectName("range_select_label")
        self.appearance_grid_layout.addWidget(self.range_select_label, 1, 0, 1, 1)
        self.total_label = QtWidgets.QLabel(self.appearance_tab)
        self.total_label.setObjectName("total_label")
        self.appearance_grid_layout.addWidget(self.total_label, 7, 0, 1, 1)
        self.ranged_line = QtWidgets.QLineEdit(self.appearance_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ranged_line.sizePolicy().hasHeightForWidth())
        self.ranged_line.setSizePolicy(sizePolicy)
        self.ranged_line.setObjectName("ranged_line")
        self.appearance_grid_layout.addWidget(self.ranged_line, 9, 1, 1, 2)
        self.seconday_color_button = QtWidgets.QPushButton(self.appearance_tab)
        self.seconday_color_button.setObjectName("seconday_color_button")
        self.appearance_grid_layout.addWidget(self.seconday_color_button, 13, 1, 1, 1)
        self.custom_range_spinbox = QtWidgets.QSpinBox(self.appearance_tab)
        self.custom_range_spinbox.setMaximum(5690)
        self.custom_range_spinbox.setProperty("value", 14)
        self.custom_range_spinbox.setObjectName("custom_range_spinbox")
        self.appearance_grid_layout.addWidget(self.custom_range_spinbox, 1, 3, 1, 1)
        self.primary_color_label = QtWidgets.QLabel(self.appearance_tab)
        self.primary_color_label.setObjectName("primary_color_label")
        self.appearance_grid_layout.addWidget(self.primary_color_label, 12, 0, 1, 1)
        self.ranged_label = QtWidgets.QLabel(self.appearance_tab)
        self.ranged_label.setObjectName("ranged_label")
        self.appearance_grid_layout.addWidget(self.ranged_label, 9, 0, 1, 1)
        self.toolbar_checkbox = QtWidgets.QCheckBox(self.appearance_tab)
        self.toolbar_checkbox.setChecked(True)
        self.toolbar_checkbox.setObjectName("toolbar_checkbox")
        self.appearance_grid_layout.addWidget(self.toolbar_checkbox, 0, 0, 1, 1)
        self.appearance_vert_layout.addLayout(self.appearance_grid_layout)
        self.pages_group_box = QtWidgets.QGroupBox(self.appearance_tab)
        self.pages_group_box.setObjectName("pages_group_box")
        self.pages_vertical_layout = QtWidgets.QHBoxLayout(self.pages_group_box)
        self.pages_vertical_layout.setObjectName("pages_vertical_layout")
        self.browser_checkbox = QtWidgets.QCheckBox(self.pages_group_box)
        self.browser_checkbox.setChecked(True)
        self.browser_checkbox.setObjectName("browser_checkbox")
        self.pages_vertical_layout.addWidget(self.browser_checkbox)
        self.overview_checkbox = QtWidgets.QCheckBox(self.pages_group_box)
        self.overview_checkbox.setChecked(True)
        self.overview_checkbox.setObjectName("overview_checkbox")
        self.pages_vertical_layout.addWidget(self.overview_checkbox)
        self.congrats_checkbox = QtWidgets.QCheckBox(self.pages_group_box)
        self.congrats_checkbox.setChecked(True)
        self.congrats_checkbox.setObjectName("congrats_checkbox")
        self.pages_vertical_layout.addWidget(self.congrats_checkbox)
        self.appearance_vert_layout.addWidget(self.pages_group_box)
        self.appearance_tab_layout.addLayout(self.appearance_vert_layout)
        self.tabs_widget.addTab(self.appearance_tab, "")
        self.decks_tab = QtWidgets.QWidget()
        self.decks_tab.setObjectName("decks_tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.decks_tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.add_remove_layout = QtWidgets.QHBoxLayout()
        self.add_remove_layout.setContentsMargins(-1, 10, -1, 10)
        self.add_remove_layout.setObjectName("add_remove_layout")
        self.add_button = QtWidgets.QPushButton(self.decks_tab)
        self.add_button.setObjectName("add_button")
        self.add_remove_layout.addWidget(self.add_button)
        self.remove_button = QtWidgets.QPushButton(self.decks_tab)
        self.remove_button.setObjectName("remove_button")
        self.add_remove_layout.addWidget(self.remove_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.add_remove_layout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.add_remove_layout)
        self.excluded_decks_list = QtWidgets.QListWidget(self.decks_tab)
        self.excluded_decks_list.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.excluded_decks_list.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.excluded_decks_list.setObjectName("excluded_decks_list")
        self.verticalLayout.addWidget(self.excluded_decks_list)
        self.tabs_widget.addTab(self.decks_tab, "")
        self.about_tab = QtWidgets.QWidget()
        self.about_tab.setObjectName("about_tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.about_tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scroll_area = QtWidgets.QScrollArea(self.about_tab)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setObjectName("scroll_area")
        self.about_scroll = QtWidgets.QWidget()
        self.about_scroll.setGeometry(QtCore.QRect(0, 0, 470, 495))
        self.about_scroll.setObjectName("about_scroll")
        self.scroll_layout = QtWidgets.QVBoxLayout(self.about_scroll)
        self.scroll_layout.setSpacing(6)
        self.scroll_layout.setObjectName("scroll_layout")
        self.about_label_header = QtWidgets.QLabel(self.about_scroll)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.about_label_header.sizePolicy().hasHeightForWidth())
        self.about_label_header.setSizePolicy(sizePolicy)
        self.about_label_header.setTextFormat(QtCore.Qt.MarkdownText)
        self.about_label_header.setWordWrap(True)
        self.about_label_header.setObjectName("about_label_header")
        self.scroll_layout.addWidget(self.about_label_header)
        self.support_buttons = QtWidgets.QHBoxLayout()
        self.support_buttons.setContentsMargins(6, 6, 6, 6)
        self.support_buttons.setObjectName("support_buttons")
        self.patreon_button = QtWidgets.QPushButton(self.about_scroll)
        self.patreon_button.setMinimumSize(QtCore.QSize(0, 42))
        self.patreon_button.setMaximumSize(QtCore.QSize(200, 16777215))
        self.patreon_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.patreon_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.patreon_button.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("raw/patreon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.patreon_button.setIcon(icon)
        self.patreon_button.setIconSize(QtCore.QSize(32, 32))
        self.patreon_button.setObjectName("patreon_button")
        self.support_buttons.addWidget(self.patreon_button)
        self.kofi_button = QtWidgets.QPushButton(self.about_scroll)
        self.kofi_button.setMinimumSize(QtCore.QSize(0, 42))
        self.kofi_button.setMaximumSize(QtCore.QSize(200, 16777215))
        self.kofi_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.kofi_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.kofi_button.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("raw/kofilogo_blue.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kofi_button.setIcon(icon1)
        self.kofi_button.setIconSize(QtCore.QSize(32, 32))
        self.kofi_button.setObjectName("kofi_button")
        self.support_buttons.addWidget(self.kofi_button)
        self.scroll_layout.addLayout(self.support_buttons)
        self.about_label_body = QtWidgets.QLabel(self.about_scroll)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.about_label_body.sizePolicy().hasHeightForWidth())
        self.about_label_body.setSizePolicy(sizePolicy)
        self.about_label_body.setTextFormat(QtCore.Qt.MarkdownText)
        self.about_label_body.setWordWrap(True)
        self.about_label_body.setObjectName("about_label_body")
        self.scroll_layout.addWidget(self.about_label_body)
        self.scroll_layout.setStretch(2, 1)
        self.scroll_area.setWidget(self.about_scroll)
        self.verticalLayout_2.addWidget(self.scroll_area)
        self.tabs_widget.addTab(self.about_tab, "")
        self.options_vert_layout.addWidget(self.tabs_widget)
        self.confirm_button_box = QtWidgets.QDialogButtonBox(OptionsDialog)
        self.confirm_button_box.setOrientation(QtCore.Qt.Horizontal)
        self.confirm_button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok|QtWidgets.QDialogButtonBox.RestoreDefaults)
        self.confirm_button_box.setObjectName("confirm_button_box")
        self.options_vert_layout.addWidget(self.confirm_button_box)

        self.retranslateUi(OptionsDialog)
        self.tabs_widget.setCurrentIndex(0)
        self.confirm_button_box.accepted.connect(OptionsDialog.accept)
        self.confirm_button_box.rejected.connect(OptionsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(OptionsDialog)

    def retranslateUi(self, OptionsDialog):
        _translate = QtCore.QCoreApplication.translate
        OptionsDialog.setWindowTitle(_translate("OptionsDialog", "Study Time Stats Options"))
        self.use_calendar_checkbox.setToolTip(_translate("OptionsDialog", "Use the start of the selected range instead of using its timespan."))
        self.use_calendar_checkbox.setText(_translate("OptionsDialog", "Use Calendar Week"))
        self.primary_color_button.setText(_translate("OptionsDialog", "Select"))
        self.hrs_label.setText(_translate("OptionsDialog", "Custom Hours Label"))
        self.week_start_label.setText(_translate("OptionsDialog", "Week-Start Day"))
        self.secondary_color_label.setText(_translate("OptionsDialog", "Secondary Color"))
        self.range_select_dropdown.setToolTip(_translate("OptionsDialog", "Time range to filter through for the ranged total stat."))
        self.range_select_dropdown.setItemText(0, _translate("OptionsDialog", "Past Week"))
        self.range_select_dropdown.setItemText(1, _translate("OptionsDialog", "Past 2 Weeks"))
        self.range_select_dropdown.setItemText(2, _translate("OptionsDialog", "Past Month"))
        self.range_select_dropdown.setItemText(3, _translate("OptionsDialog", "Past Year"))
        self.range_select_dropdown.setItemText(4, _translate("OptionsDialog", "Custom"))
        self.week_start_dropdown.setToolTip(_translate("OptionsDialog", "The day a new week should start on."))
        self.week_start_dropdown.setItemText(0, _translate("OptionsDialog", "Monday"))
        self.week_start_dropdown.setItemText(1, _translate("OptionsDialog", "Tuesday"))
        self.week_start_dropdown.setItemText(2, _translate("OptionsDialog", "Wednesday"))
        self.week_start_dropdown.setItemText(3, _translate("OptionsDialog", "Thursday"))
        self.week_start_dropdown.setItemText(4, _translate("OptionsDialog", "Friday"))
        self.week_start_dropdown.setItemText(5, _translate("OptionsDialog", "Saturday"))
        self.week_start_dropdown.setItemText(6, _translate("OptionsDialog", "Sunday"))
        self.min_label.setText(_translate("OptionsDialog", "Custom Minutes Label"))
        self.range_select_label.setText(_translate("OptionsDialog", "Selected Range"))
        self.total_label.setText(_translate("OptionsDialog", "Custom Total Text"))
        self.seconday_color_button.setText(_translate("OptionsDialog", "Select"))
        self.custom_range_spinbox.setToolTip(_translate("OptionsDialog", "Amount of days to filter the custom range."))
        self.custom_range_spinbox.setSuffix(_translate("OptionsDialog", " days"))
        self.primary_color_label.setText(_translate("OptionsDialog", "Primary Color"))
        self.ranged_label.setText(_translate("OptionsDialog", "Custom Ranged Text"))
        self.toolbar_checkbox.setToolTip(_translate("OptionsDialog", "Enables the Tools Menu shortcut for showing these options. \n"
"This window can also be opened in the Add-ons menu using the Config button."))
        self.toolbar_checkbox.setText(_translate("OptionsDialog", "Show Tools Menu Options Shortcut"))
        self.pages_group_box.setTitle(_translate("OptionsDialog", "Enabled Pages"))
        self.browser_checkbox.setText(_translate("OptionsDialog", "Deck Browser"))
        self.overview_checkbox.setText(_translate("OptionsDialog", "Overview"))
        self.congrats_checkbox.setToolTip(_translate("OptionsDialog", "The screen that shows up on the Deck Overview when all reviews are finished for the day."))
        self.congrats_checkbox.setText(_translate("OptionsDialog", "Congrats Screen"))
        self.tabs_widget.setTabText(self.tabs_widget.indexOf(self.appearance_tab), _translate("OptionsDialog", "General"))
        self.add_button.setText(_translate("OptionsDialog", "Add..."))
        self.remove_button.setText(_translate("OptionsDialog", "Remove"))
        self.tabs_widget.setTabText(self.tabs_widget.indexOf(self.decks_tab), _translate("OptionsDialog", "Excluded Decks"))
        self.about_label_header.setText(_translate("OptionsDialog", "## Study Time Stats\n"
"Adds a total and ranged study time statistic to Anki\'s main window.  \n"
"\n"
"Version: {version}  \n"
"[Releases/Changelog](https://github.com/iamjustkoi/StudyTimeStats/releases)  \n"
"[View Source](https://github.com/iamjustkoi/StudyTimeStats)  \n"
"\n"
"Have any issues or feedback? Feel free to post on the project\'s issue section on [GitHub](https://github.com/iamjustkoi/StudyTimeStats/issues)!"))
        self.patreon_button.setText(_translate("OptionsDialog", "  Become a Patron"))
        self.kofi_button.setText(_translate("OptionsDialog", "  Buy me a coffee"))
        self.about_label_body.setText(_translate("OptionsDialog", "### Text Macros\n"
"The add-on can also filter text in the custom labels input to show information based on what\'s set in the config (e.g. \"Past %range\" to \"Past Week\"). These can be used multiple times and will update whenever Anki\'s main window reloads.\n"
"\n"
"##### Available Macros:\n"
"+ **%range** - the currently selected range format (Week, 2 Weeks, Month, Year)\n"
"+ **%from_date** - range filter\'s start date using the system\'s locale (2022-06-30)\n"
"+ **%from_day** - range filter\'s starting day using a compact format (Sun)\n"
"+ **%from_full_day** - range filter\'s full start day (Sunday)\n"
"+ **%days** - total days the range filter checks against (17)\n"
"+ **%%** - returns a single % symbol and doesn\'t apply the text macro (%, %range, etc)\n"
"\n"
"<br></br>\n"
"Thanks for downloading and hope you enjoy!  \n"
"-koi  \n"
"<br></br>  \n"
"©2022 JustKoi (iamjustkoi)  \n"
"Distributed under the MIT Liecense.  "))
        self.tabs_widget.setTabText(self.tabs_widget.indexOf(self.about_tab), _translate("OptionsDialog", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OptionsDialog = QtWidgets.QDialog()
    ui = Ui_OptionsDialog()
    ui.setupUi(OptionsDialog)
    OptionsDialog.show()
    sys.exit(app.exec_())
