def create_spark_session():
    from pyspark.sql import SparkSession

    return SparkSession.builder.master("local").getOrCreate()


def create_dataframe_from_sources(spark_session, filepath):
    return spark_session.read.csv(filepath, header=True)


def generate_data_profiling(spark_session, source_df):
    from pydeequ.profiles import ColumnProfilerRunner

    profiling = ColumnProfilerRunner(spark_session) \
        .onData(source_df) \
        .run()

    for column, metrics in profiling.items():
        print(f'Column {column}:')
        print('\t', f'Completeness: {metrics.completeness}')
        print('\t', f'Number of Distinct Values: {metrics.approximateNumDistinctValues}')
        print('\t', f'Data Type: {metrics.dataType}')


def suggest_data_quality_metrics(spark_session, source_df):
    from pydeequ.suggestions import ConstraintSuggestionRunner, DEFAULT
    import json

    suggestions = ConstraintSuggestionRunner(spark_session) \
        .onData(source_df) \
        .addConstraintRule(DEFAULT()) \
        .run()

    print(json.dumps(suggestions, indent=2))


def check_data_quality_metrics(spark_session, source_df):
    from pydeequ.checks import Check, CheckLevel, ConstrainableDataTypes
    from pydeequ.verification import VerificationSuite

    check = Check(spark_session, CheckLevel.Warning, "test_data")

    check_result = VerificationSuite(spark_session) \
        .onData(source_df) \
        .addCheck(
        check.hasSize(lambda x: x >= 1000)
            .isComplete("date_id")
            .hasDataType("date_id", ConstrainableDataTypes.Integral)
            .isContainedIn("kpi_type", ["kpi_1", "kpi_2", "kpi_3"])
            .isNonNegative("kpi_value")
    ) \
        .run()

    print(f'Verification of data quality metric: {check_result.status}')


def main():
    spark_session = create_spark_session()
    source_filepath = "s3://source/data/test_data.csv"
    source_df = create_dataframe_from_sources(spark_session, source_filepath)

    generate_data_profiling(spark_session, source_df)
    suggest_data_quality_metrics(spark_session, source_df)
    check_data_quality_metrics(spark_session, source_df)


if __name__ == "__main__":
    main()
