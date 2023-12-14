import gradio as gr


def calculate_three_phase(base_power, base_voltage, subtransient_reactance_percentage):
    x_thevenin = subtransient_reactance_percentage / 100
    v_thevenin = 1
    base_current = base_power / (1.732 * base_voltage)
    per_unit_short_circuit_current = 1 / x_thevenin
    actual_short_circuit_current = per_unit_short_circuit_current * base_current
    return {
        "X-thevenin": x_thevenin,
        "V-thevenin": v_thevenin,
        "Base Current (Ib)": base_current,
        "Per Unit Short Circuit Current (Isc)": per_unit_short_circuit_current,
        "Actual Short Circuit Current (Iact)": actual_short_circuit_current
    }


def calculate_single_phase(base_power, base_voltage, subtransient_reactance_percentage):
    x_thevenin = subtransient_reactance_percentage / 100
    v_thevenin = 1
    base_current = base_power / base_voltage
    per_unit_short_circuit_current = 1 / x_thevenin
    actual_short_circuit_current = per_unit_short_circuit_current * base_current
    return {
        "X-thevenin": x_thevenin,
        "V-thevenin": v_thevenin,
        "Base Current (Ib)": base_current,
        "Per Unit Short Circuit Current (Isc)": per_unit_short_circuit_current,
        "Actual Short Circuit Current (Iact)": actual_short_circuit_current
    }


def main(phase_type, base_power, base_voltage, subtransient_reactance_percentage):
    if phase_type == 3:
        results = calculate_three_phase(
            base_power, base_voltage, subtransient_reactance_percentage)
    elif phase_type == 1:
        results = calculate_single_phase(
            base_power, base_voltage, subtransient_reactance_percentage)
    else:
        return "Invalid input. Please enter 'single' or 'three'."

    # Create output components
    output_components = [
        gr.Number(label="X-thevenin", value=results["X-thevenin"]),
        gr.Number(label="V-thevenin", value=results["V-thevenin"]),
        gr.Number(label="Base Current (Ib)",
                  value=results["Base Current (Ib)"]),
        gr.Number(label="Per Unit Short Circuit Current (Isc)",
                  value=results["Per Unit Short Circuit Current (Isc)"]),
        gr.Number(label="Actual Short Circuit Current (Iact)",
                  value=results["Actual Short Circuit Current (Iact)"])
    ]

    return results["X-thevenin"], results["V-thevenin"], results["Base Current (Ib)"], results["Per Unit Short Circuit Current (Isc)"], results["Actual Short Circuit Current (Iact)"], output_components


# Define the output components before creating the interface
output_components = [
    gr.Number(label="X-thevenin"),
    gr.Number(label="V-thevenin"),
    gr.Number(label="Base Current (Ib)"),
    gr.Number(label="Per Unit Short Circuit Current (Isc)"),
    gr.Number(label="Actual Short Circuit Current (Iact)")
]

iface = gr.Interface(
    fn=main,
    inputs=["number", "number", "number", "number"],
    outputs=output_components,
    title="SHORT CIRCUIT CALCULATOR - AN ENERGY SYSTEM PROJECT",
    description="THIS IS AN END TO END ENERGY SYSTEM PROJECT DONE TO PERFORM THE SHORT CIRCUIT CALCULATIONS FOR SINGLE PHASE AND THREE PHASE MACHINES UNDER NO LOAD CONDITIONS. \n\n"
    "WEBSITE DEVELOPMENT AND DEPLOYMENT : Pranavadhar A , Kavin Chandru , Shanthruban T\n\n"
    "DEPLOYMENT TOOL : GRADIO. \n\n"
    "BASE LANGUAGE : PYHTON \n\n"
)

iface.launch(share=True)