import * as React from 'react'
import {
    FormLabel,
    FormControl,
    FormGroup,
    FormControlLabel,
    FormHelperText,
    Checkbox,
} from '@material-ui/core'
import { withStyles } from '@material-ui/core/styles'
import { styles } from './styles'

interface Props {
    onChange: (event: React.ChangeEvent<HTMLInputElement>) => void
    label?: string
    options: Array<any>
    value?: any
    helperText?: string
    classes: {
        checkbox: string
    }
}

//checkbox for multi-select
const CheckboxInput = (props: Props) => {
    const { onChange, label, options, value, helperText, classes } = props

    return (
        <>
            <FormControl className={classes.checkbox} component="fieldset">
                <FormLabel component="legend">{label}</FormLabel>
                <FormGroup>
                    {options.map((option: any) => {
                        return (
                            <FormControlLabel
                                control={
                                    <Checkbox
                                        checked={value && value[
                                            option.value
                                        ]}
                                        onChange={onChange}
                                        name={option.value}
                                        value={option.value}
                                    />
                                }
                                label={label}
                            />
                        )
                    })}
                </FormGroup>
                <FormHelperText>{helperText}</FormHelperText>
            </FormControl>
        </>
    )
}

export default withStyles(styles)(CheckboxInput)
