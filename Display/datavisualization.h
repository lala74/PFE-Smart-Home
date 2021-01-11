#ifndef DATAVISUALIZATION_H
#define DATAVISUALIZATION_H

#include <QObject>
#include <QtCharts>

class DataVisualization : public QObject
{
    Q_OBJECT
public:
    DataVisualization();
    QList<QChart*> get_charts(const QString& sensorId);

private:
    void build_series_by_sensor_id(const QString& sensorId, QLineSeries* tempSeries, QLineSeries* humSeries);
};

#endif  // DATAVISUALIZATION_H
