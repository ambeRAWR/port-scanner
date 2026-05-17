
def report(results, target, os_result, output_file):
    if output_file == None:
        print(f"Target: {target}")
        print(f"OS: {os_result}")
        print("\n")
        print(f"PORT    STATE   SERVICE     BANNER")
        for port, state, service, banner in results:
            print(f"{port}    {state}    {service}    {banner}")

    else:
        with open(output_file, "w") as f:      
            f.write(f"Target: {target}\n")
            f.write(f"OS: {os_result}")
            f.write("\n")
            f.write(f"PORT    STATE   SERVICE     BANNER")
            for port, state, service, banner in results:
                f.write(f"{port}    {state}    {service}    {banner}")
