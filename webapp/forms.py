from django import forms
from django.forms import ValidationError
from bootstrap_modal_forms.forms import BSModalForm

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Correlation
from .fields import ListTextWidget

def validate_file_extension(value):
    if not value.name.endswith('.csv'):
         raise ValidationError("CSV format only supported.")

def validate_file_size(value):
    filesize= value.size

    if filesize > 10485760:
        raise ValidationError("The maximum allowed file size is 10 Mb")
    else:
        return value

class FrameForm(forms.Form):
    filefield = forms.FileField(validators=[validate_file_extension, validate_file_size], required=True,
                                widget=forms.ClearableFileInput(attrs={'multiple': True,'class':'upload', 'accept': ".csv"}))

class ExpImportForm(forms.Form):
    filefield = forms.FileField(validators=[validate_file_extension, validate_file_size], required=True,
                                widget=forms.ClearableFileInput(attrs={'multiple': True,'class':'upload', 'accept': ".csv"}))

def get_columns(frame):
    return frame.columns

class CorrelationForm(forms.Form):
    xcolumns_help_text = 'Choose the columns.<br/>Maximum of 4 columns allowed.'
    ycolumns_help_text = 'Choose the columns.<br/>Maximum of 4 columns allowed.'

    id = forms.CharField(required=False, widget=forms.HiddenInput())
    xcolumns = forms.MultipleChoiceField(label='X-Axis',
                                         required=True,
                                         widget=forms.SelectMultiple(attrs={'class': 'bootstrap-select'}),
                                         help_text = f'<b>Required.</b><br/>{xcolumns_help_text}')
    ycolumns = forms.MultipleChoiceField(label='Y-Axis',
                                         required=True,
                                         widget=forms.SelectMultiple(attrs={'class': 'bootstrap-select'}),
                                         help_text = f'<b>Required.</b><br/>{ycolumns_help_text}')

    def __init__(self, *args, **kwargs):
         xcolumns = kwargs.pop('xcolumns', None)
         ycolumns = kwargs.pop('ycolumns', None)
         super(CorrelationForm, self).__init__(*args, **kwargs)
         self.fields['xcolumns'].choices = [(xcolumn, xcolumn) for xcolumn in xcolumns]
         self.fields['ycolumns'].choices = [(ycolumn, ycolumn) for ycolumn in ycolumns]

    def clean_xcolumns(self):
        print('********** clean xcolumsn called ************')
        xcolumns = self.cleaned_data['xcolumns'].strip()
        if xcolumns is None:
            raise ValidationError(f'{xcolumns} is empty. Select one or more parameters.')
        elif xcolumns.len() > 4:
            raise ValidationError(f'{xcolumns} exceeded max allowable limit of 4.')
        return xcolumns

    def clean_ycolumns(self):
        ycolumns = self.cleaned_data['ycolumns'].strip()
        if ycolumns.len() > 4:
            raise ValidationError(f'{ycolumns} exceeded max allowable limit of 4.')
        return ycolumns

class HeatmapForm(forms.Form):
    pivot_cols_help_text = 'Choose pivot columns from dataset.<br/>Please limit to 4 columns.'
    value_col_help_text = 'Choose the value columns from dataset.'
    index_col_help_text = 'Choose the index columns from dataset.'
    cols_help_text = 'Choose the columns from dataset.'
    username_help_text = 'Choose the columns.<br/>Maximum of 4 columns allowed.'

    id = forms.CharField(required=False, widget=forms.HiddenInput())
    pivotCols = forms.MultipleChoiceField(label='Pivot Data',
                                       required=True,
                                       widget=forms.SelectMultiple(attrs={'class': 'bootstrap-select'}),
                                       help_text = f'<b>Required.</b><br/>{pivot_cols_help_text}')

    valueCols = forms.MultipleChoiceField(label='Values',
                              required=True,
                              widget=forms.SelectMultiple(attrs={'class': 'bootstrap-select'}),
                              help_text = f'<b>Required.</b><br/>{value_col_help_text}')

    indexCols = forms.MultipleChoiceField(label='Index',
                              required=True,
                              widget=forms.SelectMultiple(attrs={'class': 'bootstrap-select'}),
                              help_text = f'<b>Required.</b><br/>{index_col_help_text}')

    columnCols = forms.MultipleChoiceField(label='Columns',
                                          required=True,
                                          widget=forms.SelectMultiple(attrs={'class': 'bootstrap-select'}),
                                          help_text = f'<b>Required.</b><br/>{cols_help_text}')

    cma = forms.CharField(label='Color Scheme', required=False)

    def __init__(self, *args, **kwargs):
        pivotCols = kwargs.pop('pivotCols', None)
        valueCols = kwargs.pop('valueCols', None)
        indexCols = kwargs.pop('indexCols', None)
        columnCols = kwargs.pop('columnCols', None)
        cma = kwargs.pop('cma', None)

        super(HeatmapForm, self).__init__(*args, **kwargs)
        
        self.fields['pivotCols'].choices = [(pcolumn, pcolumn) for pcolumn in pivotCols]
        self.fields['valueCols'].choices = [(vcolumn, vcolumn) for vcolumn in valueCols]
        self.fields['indexCols'].choices = [(icolumn, icolumn) for icolumn in indexCols]
        self.fields['columnCols'].choices = [(icolumn, icolumn) for icolumn in columnCols]
        self.fields['cma'].widget = ListTextWidget(data_list=cma, name='cma')

    def clean_pivotCols(self):
        pivotCols = self.cleaned_data['pivotCols'].strip()
        if pivotCols is None:
            raise ValidationError(f'{pivotCols} is empty. Select one or more parameters.')
        elif pivotCols.len() > 4:
            raise ValidationError(f'{pivotCols} exceeded max allowable limit of 4.')
        return pivotCols

    def clean_valueCols(self):
        valueCols = self.cleaned_data['valueCols'].strip()
        if valueCols.len() > 1:
            raise ValidationError(f'{valueCols} is empty. Select one or more parameters.')
        return valueCols

    def clean_indexCols(self):
        indexCols = self.cleaned_data['indexCols'].strip()
        if indexCols.len() > 1:
            raise ValidationError(f'{indexCols} is empty. Select one or more parameters.')
        return indexCols

    def clean_columnCols(self):
        columnCols = self.cleaned_data['columnCols'].strip()
        if columnCols.len() > 1:
            raise ValidationError(f'{columnCols} is empty. Select one or more parameters.')
        return columnCols

    def clean_cma(self):
        cma = self.cleaned_data['cma'].strip()
        if cma is None:
            raise ValidationError(f'{cma} is required. Select one from dropdown list.')
        return cma

